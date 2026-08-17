#!/usr/bin/env python3
"""Valida las soluciones y crea los ZIP público y personalizado de la EV02."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import unicodedata
import zipfile
from pathlib import Path, PurePosixPath


SCRIPT_PATH = Path(__file__).resolve()
SOLUTION_DIR = SCRIPT_PATH.parent
WORKSHOP_DIR = SOLUTION_DIR.parent
REPO_ROOT = WORKSHOP_DIR.parents[1]
CODE = "GA3-220501093-AA3-EV02"
ARCHIVE_ROOT = CODE
PROFILE_PATH = REPO_ROOT / "perfil-aprendiz.local.json"
PUBLIC_ARCHIVE = (
    WORKSHOP_DIR
    / "03_entrega"
    / f"{CODE}_Soluciones_JavaScript_PUBLICO.zip"
)
PERSONAL_DIR = WORKSHOP_DIR / "04_entrega_personalizada.local"

SOURCE_MEMBERS = {
    SOLUTION_DIR / "codigo" / "01_figuras_planas.js": "codigo/01_figuras_planas.js",
    SOLUTION_DIR / "codigo" / "02_analisis_edades.js": "codigo/02_analisis_edades.js",
    SOLUTION_DIR / "codigo" / "03_mezclar_vectores.js": "codigo/03_mezclar_vectores.js",
    SOLUTION_DIR / "codigo" / "04_encuesta_musical.js": "codigo/04_encuesta_musical.js",
    SOLUTION_DIR / "pruebas" / "soluciones.test.js": "pruebas/soluciones.test.js",
    SOLUTION_DIR / "package.json": "package.json",
    SOLUTION_DIR / "INSTRUCCIONES.md": "INSTRUCCIONES.md",
    SOLUTION_DIR / "FUENTES_Y_DECISIONES.md": "FUENTES_Y_DECISIONES.md",
}


def run(command: list[str], *, cwd: Path = SOLUTION_DIR) -> subprocess.CompletedProcess[str]:
    print("→ " + " ".join(command))
    return subprocess.run(command, cwd=cwd, check=True, text=True)


def validate_sources() -> None:
    missing = [path for path in SOURCE_MEMBERS if not path.is_file() or path.stat().st_size == 0]
    if missing:
        raise RuntimeError(f"Faltan fuentes obligatorias: {missing}")
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js no está disponible; no se pueden validar las soluciones.")
    for path in sorted(path for path in SOURCE_MEMBERS if path.suffix == ".js" and "pruebas" not in path.parts):
        run([node, "--check", str(path)])
    run([node, "--test", str(SOLUTION_DIR / "pruebas" / "soluciones.test.js")])


def zip_info(relative: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(
        filename=f"{ARCHIVE_ROOT}/{PurePosixPath(relative).as_posix()}",
        date_time=(2026, 1, 1, 0, 0, 0),
    )
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    return info


def archive_payload(personal_data: bytes | None = None) -> dict[str, bytes]:
    payload = {
        relative: path.read_bytes()
        for path, relative in SOURCE_MEMBERS.items()
    }
    if personal_data is not None:
        payload["DATOS_DE_ENTREGA.md"] = personal_data
    return payload


def write_archive(destination: Path, payload: dict[str, bytes], *, mode: int = 0o644) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.",
        suffix=".tmp",
        dir=destination.parent,
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, "w") as archive:
            for relative in sorted(payload):
                archive.writestr(zip_info(relative), payload[relative])
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise RuntimeError("El ZIP generado contiene un componente dañado.")
        os.chmod(temporary, mode)
        os.replace(temporary, destination)
        os.chmod(destination, mode)
    finally:
        if temporary.exists():
            temporary.unlink()


def filename_fragment(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    fragment = re.sub(r"[^A-Za-z0-9]+", "_", ascii_value).strip("_")
    if not fragment:
        raise RuntimeError("El nombre del perfil no permite construir un nombre de archivo seguro.")
    return fragment


def load_profile() -> dict[str, str] | None:
    if not PROFILE_PATH.is_file():
        return None
    profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    required = (
        "nombre_completo",
        "tipo_documento",
        "documento",
        "programa",
        "institucion",
        "fecha",
    )
    missing = [key for key in required if not str(profile.get(key, "")).strip()]
    if missing:
        raise RuntimeError(f"El perfil local no contiene los campos requeridos: {missing}")
    return {key: str(value).strip() for key, value in profile.items()}


def git_ignored(relative: Path) -> bool:
    result = subprocess.run(
        ["git", "check-ignore", "--no-index", "-q", "--", relative.as_posix()],
        cwd=REPO_ROOT,
        check=False,
    )
    return result.returncode == 0


def git_tracked(relative: Path) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", "--", relative.as_posix()],
        cwd=REPO_ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def personal_markdown(profile: dict[str, str]) -> bytes:
    text = f"""# Datos de entrega

- Aprendiz: {profile['nombre_completo']}
- Tipo de documento: {profile['tipo_documento']}
- Número de documento: {profile['documento']}
- Programa: {profile['programa']}
- Institución: {profile['institucion']}
- Evidencia: {CODE}
- Fecha: {profile['fecha']}

Las cuatro soluciones incluidas fueron verificadas mediante pruebas automatizadas.
"""
    return text.encode("utf-8")


def create_personal_archive(profile: dict[str, str]) -> Path:
    personal_name = (
        f"ENTREGAR_{filename_fragment(profile['nombre_completo'])}_{CODE}.zip"
    )
    destination = PERSONAL_DIR / personal_name
    relative_destination = destination.relative_to(REPO_ROOT)
    if PERSONAL_DIR.exists() and PERSONAL_DIR.is_symlink():
        raise RuntimeError("La carpeta de entrega personalizada no puede ser un enlace simbólico.")
    if not git_ignored(relative_destination):
        raise RuntimeError("La entrega personalizada no está protegida por .gitignore.")
    if git_tracked(relative_destination):
        raise RuntimeError("La entrega personalizada aparece registrada en Git.")
    PERSONAL_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(PERSONAL_DIR, 0o700)
    unexpected = [path for path in PERSONAL_DIR.iterdir() if path != destination]
    if unexpected:
        raise RuntimeError(
            "La carpeta personalizada debe contener un único archivo; se encontraron: "
            f"{[path.name for path in unexpected]}"
        )
    write_archive(destination, archive_payload(personal_markdown(profile)), mode=0o600)
    contents = list(PERSONAL_DIR.iterdir())
    if contents != [destination]:
        raise RuntimeError("La carpeta personalizada no contiene exactamente el ZIP esperado.")
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--solo-publico",
        action="store_true",
        help="omite la edición personalizada aunque exista el perfil local",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validate_sources()
    write_archive(PUBLIC_ARCHIVE, archive_payload())
    print(f"Creado ZIP público: {PUBLIC_ARCHIVE}")
    profile = None if args.solo_publico else load_profile()
    if profile is not None:
        personal = create_personal_archive(profile)
        print(f"Creado un único ZIP personalizado local: {personal}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
