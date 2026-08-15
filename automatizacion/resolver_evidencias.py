#!/usr/bin/env python3
"""Regenera, valida y audita las evidencias contenidas en este repositorio."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ElementTree
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
PRIVATE_BLOCKLIST = REPO_ROOT / ".privacidad.local"
SKIPPED_DIRS = {".git", ".venv", "__pycache__"}
TEXT_SUFFIXES = {
    ".cfg",
    ".csv",
    ".html",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".rels",
    ".rst",
    ".sh",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
OFFICE_SUFFIXES = {".docx", ".pptx", ".xlsx"}
ALLOWED_LONG_NUMBERS = {"240202501"}  # Código público del resultado de aprendizaje.


@dataclass(frozen=True)
class PdfExport:
    source: Path
    destination: Path


@dataclass(frozen=True)
class Workshop:
    number: int
    code: str
    title: str
    directory: Path
    generator: Path
    requirements: Path
    outputs: tuple[Path, ...]
    exports: tuple[PdfExport, ...]


def workshop_path(folder: str, relative: str) -> Path:
    return REPO_ROOT / "talleres" / folder / relative


FIRST_FOLDER = "01-GA2-240202501-AA1-EV03-cronica-alan-turing"
SECOND_FOLDER = "02-GA2-240202501-AA2-EV02-presentacion-monserrate"

WORKSHOPS = {
    1: Workshop(
        number=1,
        code="GA2-240202501-AA1-EV03",
        title="Crónica en inglés sobre Alan Turing",
        directory=REPO_ROOT / "talleres" / FIRST_FOLDER,
        generator=workshop_path(FIRST_FOLDER, "02_solucion/generar_entrega.py"),
        requirements=workshop_path(FIRST_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(FIRST_FOLDER, "03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.docx"),
            workshop_path(FIRST_FOLDER, "03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.pdf"),
            workshop_path(FIRST_FOLDER, "03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.txt"),
        ),
        exports=(
            PdfExport(
                source=workshop_path(
                    FIRST_FOLDER,
                    "03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.docx",
                ),
                destination=workshop_path(
                    FIRST_FOLDER,
                    "03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.pdf",
                ),
            ),
        ),
    ),
    2: Workshop(
        number=2,
        code="GA2-240202501-AA2-EV02",
        title="Presentación en inglés sobre Monserrate",
        directory=REPO_ROOT / "talleres" / SECOND_FOLDER,
        generator=workshop_path(SECOND_FOLDER, "02_solucion/generar_presentacion.py"),
        requirements=workshop_path(SECOND_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(
                SECOND_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pptx",
            ),
            workshop_path(
                SECOND_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pdf",
            ),
            workshop_path(
                SECOND_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.docx",
            ),
            workshop_path(
                SECOND_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.pdf",
            ),
        ),
        exports=(
            PdfExport(
                source=workshop_path(
                    SECOND_FOLDER,
                    "03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pptx",
                ),
                destination=workshop_path(
                    SECOND_FOLDER,
                    "03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pdf",
                ),
            ),
            PdfExport(
                source=workshop_path(
                    SECOND_FOLDER,
                    "03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.docx",
                ),
                destination=workshop_path(
                    SECOND_FOLDER,
                    "03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.pdf",
                ),
            ),
        ),
    ),
}

EXPECTED_PDF_PAGES = {
    WORKSHOPS[1].outputs[1]: 3,
    WORKSHOPS[2].outputs[1]: 8,
    WORKSHOPS[2].outputs[3]: 8,
}
EXPECTED_PPTX_SLIDES = {WORKSHOPS[2].outputs[0]: 8}


def run(command: list[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    printable = " ".join(command)
    print(f"→ {printable}")
    return subprocess.run(
        command,
        cwd=REPO_ROOT,
        check=True,
        text=True,
        capture_output=capture,
    )


def generation_python() -> Path:
    local_python = REPO_ROOT / ".venv" / "bin" / "python"
    return local_python if local_python.is_file() else Path(sys.executable)


def prepare_environment() -> None:
    virtualenv = REPO_ROOT / ".venv"
    if not virtualenv.exists():
        run([sys.executable, "-m", "venv", str(virtualenv)])
    python = virtualenv / "bin" / "python"
    run([str(python), "-m", "pip", "install", "--upgrade", "pip"])
    for requirements in dict.fromkeys(item.requirements for item in WORKSHOPS.values()):
        run([str(python), "-m", "pip", "install", "-r", str(requirements)])
    print("✓ Entorno de generación preparado.")


def export_pdf(item: PdfExport) -> None:
    office = shutil.which("libreoffice") or shutil.which("soffice")
    if not office:
        raise RuntimeError("LibreOffice no está disponible; no se puede generar el PDF.")
    if not item.source.is_file():
        raise RuntimeError(f"No existe la fuente para exportar: {item.source}")
    item.destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".exportacion-",
        dir=item.destination.parent,
    ) as temp_name:
        temp_dir = Path(temp_name)
        run(
            [
                office,
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                str(temp_dir),
                str(item.source),
            ]
        )
        generated = temp_dir / f"{item.source.stem}.pdf"
        if not generated.is_file() or generated.stat().st_size == 0:
            raise RuntimeError(f"LibreOffice no creó el PDF esperado: {generated}")
        os.replace(generated, item.destination)


def validate_zip(path: Path) -> None:
    if not zipfile.is_zipfile(path):
        raise RuntimeError(f"El archivo Office no es un ZIP válido: {path}")
    with zipfile.ZipFile(path) as archive:
        damaged_member = archive.testzip()
        if damaged_member:
            raise RuntimeError(f"Componente dañado en {path}: {damaged_member}")
        members = set(archive.namelist())
        required = {"[Content_Types].xml"}
        if path.suffix.lower() == ".docx":
            required.add("word/document.xml")
        elif path.suffix.lower() == ".pptx":
            required.add("ppt/presentation.xml")
        missing = required - members
        if missing:
            raise RuntimeError(f"Partes obligatorias ausentes en {path}: {sorted(missing)}")
        unsafe = [
            member
            for member in members
            if member.lower().endswith("vbaproject.bin")
            or "/embeddings/" in member.lower()
        ]
        if unsafe:
            raise RuntimeError(f"El archivo contiene macros u objetos incrustados: {path}")
        expected_slides = EXPECTED_PPTX_SLIDES.get(path)
        if expected_slides is not None:
            slides = sum(
                bool(re.fullmatch(r"ppt/slides/slide\d+\.xml", member))
                for member in members
            )
            if slides != expected_slides:
                raise RuntimeError(
                    f"Cantidad de diapositivas inesperada en {path}: "
                    f"{slides}, se esperaban {expected_slides}."
                )


def validate_pdf(path: Path) -> None:
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        raise RuntimeError("pdfinfo no está disponible; la validación PDF no puede continuar.")
    result = run([pdfinfo, str(path)], capture=True)
    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, flags=re.MULTILINE)
    if not match or int(match.group(1)) < 1:
        raise RuntimeError(f"El PDF no contiene páginas válidas: {path}")
    pages = int(match.group(1))
    expected_pages = EXPECTED_PDF_PAGES.get(path)
    if expected_pages is not None and pages != expected_pages:
        raise RuntimeError(
            f"Cantidad de páginas inesperada en {path}: "
            f"{pages}, se esperaban {expected_pages}."
        )
    encrypted = re.search(r"^Encrypted:\s+(\S+)", result.stdout, flags=re.MULTILINE)
    if encrypted and encrypted.group(1).lower() != "no":
        raise RuntimeError(f"El PDF está cifrado y no puede auditarse completamente: {path}")


def validate_workshop(workshop: Workshop) -> None:
    for output in workshop.outputs:
        if not output.is_file() or output.stat().st_size == 0:
            raise RuntimeError(f"Entregable ausente o vacío: {output}")
        if output.suffix.lower() in OFFICE_SUFFIXES:
            validate_zip(output)
        elif output.suffix.lower() == ".pdf":
            validate_pdf(output)
    print(f"✓ Taller {workshop.number}: {len(workshop.outputs)} entregables válidos.")


def resolve_workshop(workshop: Workshop) -> None:
    print(f"\nResolviendo taller {workshop.number}: {workshop.title}")
    run([str(generation_python()), str(workshop.generator)])
    for export in workshop.exports:
        export_pdf(export)
    validate_workshop(workshop)


def repository_files() -> Iterable[Path]:
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(REPO_ROOT)
        if any(part in SKIPPED_DIRS for part in relative.parts):
            continue
        if path == PRIVATE_BLOCKLIST:
            continue
        yield path


def decode_text(data: bytes) -> str:
    for encoding in ("utf-8", "utf-16", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def xml_human_text(data: bytes) -> tuple[str, str]:
    """Return visible/property text and external targets without OOXML geometry IDs."""
    try:
        root = ElementTree.fromstring(data)
    except ElementTree.ParseError:
        return decode_text(data), ""
    text_values: list[str] = []
    external_targets: list[str] = []
    property_tags = {
        "category",
        "company",
        "contentStatus",
        "creator",
        "description",
        "keywords",
        "lastModifiedBy",
        "lpstr",
        "lpwstr",
        "manager",
        "subject",
        "t",
        "title",
    }
    for element in root.iter():
        local_name = element.tag.rsplit("}", 1)[-1]
        if local_name in property_tags and element.text:
            text_values.append(element.text)
        if local_name == "Relationship" and element.attrib.get("TargetMode") == "External":
            target = element.attrib.get("Target")
            if target:
                external_targets.append(target)
    return "\n".join(text_values), "\n".join(external_targets)


def relevant_pdf_metadata(text: str) -> str:
    allowed_fields = {"Title", "Subject", "Keywords", "Author"}
    values: list[str] = []
    for line in text.splitlines():
        field, separator, value = line.partition(":")
        if separator and field.strip() in allowed_fields:
            values.append(value.strip())
    return "\n".join(values)


def extracted_parts(path: Path) -> Iterable[tuple[str, str]]:
    suffix = path.suffix.lower()
    yield "ruta", str(path.relative_to(REPO_ROOT))
    if suffix in TEXT_SUFFIXES:
        yield "contenido", path.read_text(encoding="utf-8", errors="replace")
        return
    if suffix in OFFICE_SUFFIXES:
        if not zipfile.is_zipfile(path):
            yield "archivo", "FORMATO OFFICE DAÑADO"
            return
        with zipfile.ZipFile(path) as archive:
            for member in archive.infolist():
                if member.is_dir() or not member.filename.lower().endswith((".xml", ".rels", ".txt")):
                    continue
                visible_text, external_targets = xml_human_text(archive.read(member))
                if visible_text:
                    yield member.filename, visible_text
                if external_targets:
                    yield f"{member.filename} — relaciones externas", external_targets
        return
    if suffix == ".pdf":
        pdftotext = shutil.which("pdftotext")
        pdfinfo = shutil.which("pdfinfo")
        if not pdftotext or not pdfinfo:
            raise RuntimeError("pdftotext y pdfinfo son obligatorios para auditar archivos PDF.")
        text_result = run([pdftotext, str(path), "-"], capture=True)
        info_result = run([pdfinfo, str(path)], capture=True)
        yield "texto PDF", text_result.stdout
        metadata = relevant_pdf_metadata(info_result.stdout)
        if metadata:
            yield "metadatos PDF", metadata


def load_private_terms(extra_path: Path | None) -> list[str]:
    values: list[str] = []
    env_values = os.environ.get("EVIDENCIAS_BLOCKLIST", "")
    values.extend(part.strip() for part in env_values.split(os.pathsep) if part.strip())
    path = extra_path or (PRIVATE_BLOCKLIST if PRIVATE_BLOCKLIST.is_file() else None)
    if path:
        values.extend(
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
    return list(dict.fromkeys(values))


def built_in_private_terms() -> tuple[str, ...]:
    """Build profile-field terms without publishing them as readable repository text."""
    code_points = (
        (65, 68, 83, 79),
        (102, 105, 99, 104, 97),
        (99, 101, 100, 117, 108, 97),
        (99, 233, 100, 117, 108, 97),
    )
    return tuple("".join(chr(code) for code in term) for term in code_points)


def privacy_findings(
    text: str,
    private_terms: list[str],
    *,
    check_long_numbers: bool = True,
) -> list[str]:
    findings: list[str] = []
    if check_long_numbers:
        for number in re.findall(r"(?<![\w-])\d{7,12}(?![\w-])", text):
            if number not in ALLOWED_LONG_NUMBERS:
                findings.append(f"secuencia numérica de alto riesgo ({len(number)} dígitos)")
    if re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text, flags=re.IGNORECASE):
        findings.append("dirección de correo")
    secret_patterns = (
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"github_pat_[A-Za-z0-9_]{20,}",
        r"gh[opsu]_[A-Za-z0-9]{20,}",
        r"AKIA[0-9A-Z]{16}",
    )
    if any(re.search(pattern, text) for pattern in secret_patterns):
        findings.append("credencial o clave privada")
    local_path_patterns = (
        "file:" + r"/+",
        "/" + "home" + "/",
        r"[A-Za-z]:\\" + "Users" + r"\\",
    )
    if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in local_path_patterns):
        findings.append("ruta local de usuario")
    folded_text = text.casefold()
    for term in built_in_private_terms():
        if re.search(rf"(?<!\w){re.escape(term.casefold())}(?!\w)", folded_text):
            findings.append("campo de perfil no autorizado")
    for term in private_terms:
        if term.casefold() in folded_text:
            findings.append("valor incluido en la lista privada local")
    return list(dict.fromkeys(findings))


def audit_privacy(extra_path: Path | None = None) -> None:
    private_terms = load_private_terms(extra_path)
    findings: list[str] = []
    checked = 0
    for path in repository_files():
        for component, text in extracted_parts(path):
            checked += 1
            for finding in privacy_findings(
                text,
                private_terms,
                check_long_numbers="relaciones externas" not in component,
            ):
                findings.append(f"{path.relative_to(REPO_ROOT)} [{component}]: {finding}")
    if findings:
        print("\n✗ La auditoría de privacidad encontró riesgos:", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        raise RuntimeError(f"Auditoría fallida con {len(findings)} hallazgo(s).")
    print(f"✓ Auditoría de privacidad aprobada ({checked} componentes revisados).")


def selected_workshops(args: argparse.Namespace) -> list[Workshop]:
    if getattr(args, "todos", False):
        return list(WORKSHOPS.values())
    number = getattr(args, "taller", None)
    if number is None:
        raise RuntimeError("Indique --taller N o --todos.")
    return [WORKSHOPS[number]]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resolutor reproducible y auditor de evidencias SENA.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("listar", help="muestra los talleres registrados")
    subparsers.add_parser("preparar", help="crea el entorno e instala dependencias")

    for command, help_text in (
        ("resolver", "regenera, exporta, valida y audita"),
        ("validar", "comprueba los entregables existentes"),
    ):
        subparser = subparsers.add_parser(command, help=help_text)
        selection = subparser.add_mutually_exclusive_group(required=True)
        selection.add_argument("--taller", type=int, choices=sorted(WORKSHOPS))
        selection.add_argument("--todos", action="store_true")

    audit_parser = subparsers.add_parser(
        "auditar",
        help="busca identificadores, correos y secretos en texto y documentos",
    )
    audit_parser.add_argument(
        "--lista-privada",
        type=Path,
        help="archivo local ignorado por Git, con un valor confidencial por línea",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "listar":
            for workshop in WORKSHOPS.values():
                print(f"{workshop.number}: {workshop.code} — {workshop.title}")
        elif args.command == "preparar":
            prepare_environment()
        elif args.command == "resolver":
            for workshop in selected_workshops(args):
                resolve_workshop(workshop)
            audit_privacy()
        elif args.command == "validar":
            for workshop in selected_workshops(args):
                validate_workshop(workshop)
        elif args.command == "auditar":
            audit_privacy(args.lista_privada)
    except (OSError, RuntimeError, subprocess.CalledProcessError, zipfile.BadZipFile) as error:
        print(f"✗ {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
