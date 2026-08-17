#!/usr/bin/env python3
"""Regenera, valida y audita las evidencias contenidas en este repositorio."""

from __future__ import annotations

import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ElementTree
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
PRIVATE_BLOCKLIST = REPO_ROOT / ".privacidad.local"
LOCAL_PROFILE_NAME = "perfil-aprendiz.local.json"
TEXT_SUFFIXES = {
    ".cfg",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".md",
    ".py",
    ".psc",
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
ARCHIVE_SUFFIXES = {".zip"}
ALLOWED_LONG_NUMBERS = {
    "220501093",
    "240202501",
}  # Códigos públicos de resultados de aprendizaje.


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
THIRD_FOLDER = "03-GA2-240202501-AA2-EV03-correo-solicitud-empleo"
FOURTH_FOLDER = "04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto"
FIFTH_FOLDER = "05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos"
SIXTH_FOLDER = "06-GA3-220501093-AA3-EV01-bases-teoricas-javascript"
SEVENTH_FOLDER = "07-GA3-220501093-AA3-EV02-estructuras-almacenamiento-javascript"

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
    3: Workshop(
        number=3,
        code="GA2-240202501-AA2-EV03",
        title="Correo en inglés de solicitud de empleo",
        directory=REPO_ROOT / "talleres" / THIRD_FOLDER,
        generator=workshop_path(THIRD_FOLDER, "02_solucion/generar_entrega.py"),
        requirements=workshop_path(THIRD_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(
                THIRD_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.docx",
            ),
            workshop_path(
                THIRD_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.pdf",
            ),
            workshop_path(
                THIRD_FOLDER,
                "03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.txt",
            ),
        ),
        exports=(
            PdfExport(
                source=workshop_path(
                    THIRD_FOLDER,
                    "03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.docx",
                ),
                destination=workshop_path(
                    THIRD_FOLDER,
                    "03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.pdf",
                ),
            ),
        ),
    ),
    4: Workshop(
        number=4,
        code="GA3-220501093-AA2-EV01",
        title="Algoritmos de edad y año bisiesto",
        directory=REPO_ROOT / "talleres" / FOURTH_FOLDER,
        generator=workshop_path(FOURTH_FOLDER, "02_solucion/generar_entrega.py"),
        requirements=workshop_path(FOURTH_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(
                FOURTH_FOLDER,
                "03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.docx",
            ),
            workshop_path(
                FOURTH_FOLDER,
                "03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.pdf",
            ),
        ),
        exports=(
            PdfExport(
                source=workshop_path(
                    FOURTH_FOLDER,
                    "03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.docx",
                ),
                destination=workshop_path(
                    FOURTH_FOLDER,
                    "03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.pdf",
                ),
            ),
        ),
    ),
    5: Workshop(
        number=5,
        code="GA3-220501093-AA2-EV03",
        title="Funciones y procedimientos en la solución de algoritmos",
        directory=REPO_ROOT / "talleres" / FIFTH_FOLDER,
        generator=workshop_path(FIFTH_FOLDER, "02_solucion/generar_entrega.py"),
        requirements=workshop_path(FIFTH_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(
                FIFTH_FOLDER,
                "03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.docx",
            ),
            workshop_path(
                FIFTH_FOLDER,
                "03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.pdf",
            ),
            workshop_path(
                FIFTH_FOLDER,
                "03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.zip",
            ),
        ),
        exports=(
            PdfExport(
                source=workshop_path(
                    FIFTH_FOLDER,
                    "03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.docx",
                ),
                destination=workshop_path(
                    FIFTH_FOLDER,
                    "03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.pdf",
                ),
            ),
        ),
    ),
    6: Workshop(
        number=6,
        code="GA3-220501093-AA3-EV01",
        title="Bases teóricas de estructuras de almacenamiento en memoria",
        directory=REPO_ROOT / "talleres" / SIXTH_FOLDER,
        generator=workshop_path(SIXTH_FOLDER, "02_solucion/generar_entrega.py"),
        requirements=workshop_path(SIXTH_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(
                SIXTH_FOLDER,
                "03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.docx",
            ),
            workshop_path(
                SIXTH_FOLDER,
                "03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.pdf",
            ),
        ),
        exports=(
            PdfExport(
                source=workshop_path(
                    SIXTH_FOLDER,
                    "03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.docx",
                ),
                destination=workshop_path(
                    SIXTH_FOLDER,
                    "03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.pdf",
                ),
            ),
        ),
    ),
    7: Workshop(
        number=7,
        code="GA3-220501093-AA3-EV02",
        title="Resolución de problemas con estructuras de almacenamiento",
        directory=REPO_ROOT / "talleres" / SEVENTH_FOLDER,
        generator=workshop_path(SEVENTH_FOLDER, "02_solucion/generar_entrega.py"),
        requirements=workshop_path(SEVENTH_FOLDER, "02_solucion/requirements.txt"),
        outputs=(
            workshop_path(
                SEVENTH_FOLDER,
                "03_entrega/GA3-220501093-AA3-EV02_Soluciones_JavaScript_PUBLICO.zip",
            ),
        ),
        exports=(),
    ),
}

EXPECTED_PDF_PAGES = {
    WORKSHOPS[1].outputs[1]: 3,
    WORKSHOPS[2].outputs[1]: 8,
    WORKSHOPS[2].outputs[3]: 8,
    WORKSHOPS[3].outputs[1]: 1,
    WORKSHOPS[4].outputs[1]: 10,
    WORKSHOPS[5].outputs[1]: 33,
    WORKSHOPS[6].outputs[1]: 12,
}
EXPECTED_PPTX_SLIDES = {WORKSHOPS[2].outputs[0]: 8}
EXPECTED_DOCX_IMAGES = {
    WORKSHOPS[4].outputs[0]: 2,
    WORKSHOPS[5].outputs[0]: 10,
    WORKSHOPS[6].outputs[0]: 4,
}
EXPECTED_PUBLIC_AUTHORS = {
    WORKSHOPS[5].outputs[0]: "Entrega académica pública",
    WORKSHOPS[5].outputs[1]: "Entrega académica pública",
    WORKSHOPS[6].outputs[0]: "Entrega académica pública",
    WORKSHOPS[6].outputs[1]: "Entrega académica pública",
}
EXPECTED_PDF_TEXT_TERMS = {
    WORKSHOPS[6].outputs[1]: (
        "Lenguajes compilados e interpretados",
        "Características principales de JavaScript",
        "Tipos de datos primitivos",
        "Operadores en JavaScript",
        "Referencias",
    ),
}
EXPECTED_TEXT_WORD_RANGES = {WORKSHOPS[3].outputs[2]: (200, 400)}
EXPECTED_DOCX_FORMATS = {
    WORKSHOPS[3].outputs[0]: {
        "font": "Arial",
        "size_half_points": "24",
        "line_twips": "360",
    }
}

FIFTH_ARCHIVE_ROOT = WORKSHOPS[5].code
SEVENTH_ARCHIVE_ROOT = WORKSHOPS[7].code
SEVENTH_SOURCE_RELATIVES = (
    "codigo/01_figuras_planas.js",
    "codigo/02_analisis_edades.js",
    "codigo/03_mezclar_vectores.js",
    "codigo/04_encuesta_musical.js",
    "pruebas/soluciones.test.js",
    "package.json",
    "INSTRUCCIONES.md",
    "FUENTES_Y_DECISIONES.md",
)
EXPECTED_DELIVERY_ZIP_MEMBERS = {
    WORKSHOPS[5].outputs[2]: {
        f"{FIFTH_ARCHIVE_ROOT}/LEAME.txt",
        f"{FIFTH_ARCHIVE_ROOT}/{WORKSHOPS[5].outputs[0].name}",
        *{
            f"{FIFTH_ARCHIVE_ROOT}/pseudocodigo/{number:02d}_{slug}.psc"
            for number, slug in (
                (1, "ritmo_maraton"),
                (2, "celsius_fahrenheit"),
                (3, "nota_primer_parcial"),
                (4, "duplicar_capital"),
                (5, "numeros_menores_igual_25"),
                (6, "camisas_dolares_pesos"),
                (7, "consumos_restaurante"),
                (8, "siguiente_segundo"),
                (9, "producto_1_hasta_n"),
                (10, "tabla_multiplicar_decreciente"),
            )
        },
        *{
            f"{FIFTH_ARCHIVE_ROOT}/diagramas/{number:02d}_{slug}.png"
            for number, slug in (
                (1, "ritmo_maraton"),
                (2, "celsius_fahrenheit"),
                (3, "nota_primer_parcial"),
                (4, "duplicar_capital"),
                (5, "numeros_menores_igual_25"),
                (6, "camisas_dolares_pesos"),
                (7, "consumos_restaurante"),
                (8, "siguiente_segundo"),
                (9, "producto_1_hasta_n"),
                (10, "tabla_multiplicar_decreciente"),
            )
        },
    },
    WORKSHOPS[7].outputs[0]: {
        f"{SEVENTH_ARCHIVE_ROOT}/{relative}"
        for relative in SEVENTH_SOURCE_RELATIVES
    },
}


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
        expected_images = EXPECTED_DOCX_IMAGES.get(path)
        if expected_images is not None:
            images = sum(
                member.startswith("word/media/") and not member.endswith("/")
                for member in members
            )
            if images != expected_images:
                raise RuntimeError(
                    f"Cantidad de imágenes inesperada en {path}: "
                    f"{images}, se esperaban {expected_images}."
                )
        expected_author = EXPECTED_PUBLIC_AUTHORS.get(path)
        if expected_author is not None:
            core_path = "docProps/core.xml"
            if core_path not in members:
                raise RuntimeError(f"El DOCX no contiene metadatos verificables: {path}")
            core = ElementTree.fromstring(archive.read(core_path))
            creator_tag = "{http://purl.org/dc/elements/1.1/}creator"
            modifier_tag = (
                "{http://schemas.openxmlformats.org/package/2006/metadata/core-properties}"
                "lastModifiedBy"
            )
            creators = [
                element.text or ""
                for element in core.iter()
                if element.tag in {creator_tag, modifier_tag}
            ]
            if not creators or any(value != expected_author for value in creators):
                raise RuntimeError(
                    f"Autor público inesperado en {path}: {creators!r}."
                )


def validate_delivery_archive(path: Path) -> None:
    if not zipfile.is_zipfile(path):
        raise RuntimeError(f"El entregable ZIP no es válido: {path}")
    with zipfile.ZipFile(path) as archive:
        damaged_member = archive.testzip()
        if damaged_member:
            raise RuntimeError(f"Componente dañado en {path}: {damaged_member}")
        entries = [member for member in archive.infolist() if not member.is_dir()]
        names = {member.filename for member in entries}
        expected = EXPECTED_DELIVERY_ZIP_MEMBERS.get(path)
        if expected is not None and names != expected:
            missing = sorted(expected - names)
            unexpected = sorted(names - expected)
            raise RuntimeError(
                f"Contenido inesperado en {path}: faltan {missing}; sobran {unexpected}."
            )
        unsafe: list[str] = []
        for member in entries:
            relative = PurePosixPath(member.filename)
            unix_mode = member.external_attr >> 16
            is_symlink = unix_mode & 0o170000 == 0o120000
            if (
                relative.is_absolute()
                or ".." in relative.parts
                or member.flag_bits & 0x1
                or is_symlink
            ):
                unsafe.append(member.filename)
        if unsafe:
            raise RuntimeError(f"El ZIP contiene rutas o entradas inseguras: {unsafe}")

        if path == WORKSHOPS[5].outputs[2]:
            archived_docx = (
                f"{FIFTH_ARCHIVE_ROOT}/{WORKSHOPS[5].outputs[0].name}"
            )
            if archive.read(archived_docx) != WORKSHOPS[5].outputs[0].read_bytes():
                raise RuntimeError(
                    "El DOCX incluido en el ZIP no coincide con la entrega pública."
                )
            for name in names:
                if name.endswith(".psc") and not archive.read(name).strip():
                    raise RuntimeError(f"Pseudocódigo vacío dentro del ZIP: {name}")
        if path == WORKSHOPS[7].outputs[0]:
            for relative in SEVENTH_SOURCE_RELATIVES:
                archived_name = f"{SEVENTH_ARCHIVE_ROOT}/{relative}"
                source = workshop_path(SEVENTH_FOLDER, f"02_solucion/{relative}")
                if archive.read(archived_name) != source.read_bytes():
                    raise RuntimeError(
                        f"El componente {relative} del ZIP no coincide con su fuente."
                    )
            javascript_files = [
                name
                for name in names
                if name.startswith(f"{SEVENTH_ARCHIVE_ROOT}/codigo/")
                and name.endswith(".js")
            ]
            if len(javascript_files) != 4:
                raise RuntimeError(
                    "El ZIP público no contiene exactamente las cuatro soluciones JavaScript."
                )
            if any(not archive.read(name).strip() for name in javascript_files):
                raise RuntimeError("El ZIP público contiene una solución JavaScript vacía.")


def validate_javascript_workshop(workshop: Workshop) -> None:
    if workshop.number != 7:
        return
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Node.js no está disponible para validar el taller 7.")
    solution = workshop.directory / "02_solucion"
    for relative in SEVENTH_SOURCE_RELATIVES:
        if relative.startswith("codigo/") and relative.endswith(".js"):
            run([node, "--check", str(solution / relative)])
    run([node, "--test", str(solution / "pruebas/soluciones.test.js")])


def validate_docx_format(path: Path) -> None:
    expected = EXPECTED_DOCX_FORMATS.get(path)
    if expected is None:
        return

    word_namespace = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

    def tag(name: str) -> str:
        return f"{{{word_namespace}}}{name}"

    def attribute(name: str) -> str:
        return f"{{{word_namespace}}}{name}"

    with zipfile.ZipFile(path) as archive:
        root = ElementTree.fromstring(archive.read("word/document.xml"))

    text_runs = 0
    wrong_fonts: set[str] = set()
    wrong_sizes: set[str] = set()
    for run in root.iter(tag("r")):
        visible_text = "".join(
            node.text or "" for node in run.iter(tag("t"))
        ).strip()
        if not visible_text:
            continue
        text_runs += 1
        properties = run.find(tag("rPr"))
        fonts = properties.find(tag("rFonts")) if properties is not None else None
        size = properties.find(tag("sz")) if properties is not None else None
        font_name = fonts.get(attribute("ascii"), "") if fonts is not None else ""
        font_size = size.get(attribute("val"), "") if size is not None else ""
        if font_name != expected["font"]:
            wrong_fonts.add(font_name or "sin definir")
        if font_size != expected["size_half_points"]:
            wrong_sizes.add(font_size or "sin definir")

    wrong_lines: set[str] = set()
    text_paragraphs = 0
    for paragraph in root.iter(tag("p")):
        visible_text = "".join(
            node.text or "" for node in paragraph.iter(tag("t"))
        ).strip()
        if not visible_text:
            continue
        text_paragraphs += 1
        properties = paragraph.find(tag("pPr"))
        spacing = properties.find(tag("spacing")) if properties is not None else None
        line_value = spacing.get(attribute("line"), "") if spacing is not None else ""
        line_rule = spacing.get(attribute("lineRule"), "") if spacing is not None else ""
        if line_value != expected["line_twips"] or line_rule != "auto":
            wrong_lines.add(f"{line_value or 'sin definir'}/{line_rule or 'sin definir'}")

    if not text_runs or not text_paragraphs:
        raise RuntimeError(f"El DOCX no contiene texto verificable: {path}")
    if wrong_fonts or wrong_sizes or wrong_lines:
        details = []
        if wrong_fonts:
            details.append(f"fuentes {sorted(wrong_fonts)}")
        if wrong_sizes:
            details.append(f"tamaños {sorted(wrong_sizes)}")
        if wrong_lines:
            details.append(f"interlineados {sorted(wrong_lines)}")
        raise RuntimeError(
            f"Formato académico inesperado en {path}: {', '.join(details)}."
        )


def validate_text_word_count(path: Path) -> None:
    expected = EXPECTED_TEXT_WORD_RANGES.get(path)
    if expected is None:
        return
    text = path.read_text(encoding="utf-8")
    _, separator, message = text.partition("\n\n")
    countable_text = message if separator else text
    count = len(re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", countable_text))
    minimum, maximum = expected
    if not minimum <= count <= maximum:
        raise RuntimeError(
            f"Extensión inesperada en {path}: {count} palabras; "
            f"se esperaban entre {minimum} y {maximum}."
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
    expected_author = EXPECTED_PUBLIC_AUTHORS.get(path)
    if expected_author is not None:
        author = re.search(r"^Author:\s*(.*)$", result.stdout, flags=re.MULTILINE)
        if not author or author.group(1).strip() != expected_author:
            actual = author.group(1).strip() if author else "ausente"
            raise RuntimeError(
                f"Autor público inesperado en {path}: {actual!r}."
            )
    expected_terms = EXPECTED_PDF_TEXT_TERMS.get(path)
    if expected_terms:
        pdftotext = shutil.which("pdftotext")
        if not pdftotext:
            raise RuntimeError(
                "pdftotext no está disponible; no se puede verificar la cobertura del PDF."
            )
        extracted = run([pdftotext, str(path), "-"], capture=True).stdout.casefold()
        missing_terms = [term for term in expected_terms if term.casefold() not in extracted]
        if missing_terms:
            raise RuntimeError(
                f"El PDF no contiene secciones obligatorias: {missing_terms}."
            )


def validate_workshop(workshop: Workshop) -> None:
    for output in workshop.outputs:
        if not output.is_file() or output.stat().st_size == 0:
            raise RuntimeError(f"Entregable ausente o vacío: {output}")
        if output.suffix.lower() in OFFICE_SUFFIXES:
            validate_zip(output)
            if output.suffix.lower() == ".docx":
                validate_docx_format(output)
        elif output.suffix.lower() == ".pdf":
            validate_pdf(output)
        elif output.suffix.lower() == ".txt":
            validate_text_word_count(output)
        elif output.suffix.lower() in ARCHIVE_SUFFIXES:
            validate_delivery_archive(output)
    validate_javascript_workshop(workshop)
    print(f"✓ Taller {workshop.number}: {len(workshop.outputs)} entregables válidos.")


def resolve_workshop(workshop: Workshop) -> None:
    print(f"\nResolviendo taller {workshop.number}: {workshop.title}")
    run([str(generation_python()), str(workshop.generator)])
    for export in workshop.exports:
        export_pdf(export)
    validate_workshop(workshop)


def git_relative_files(*options: str) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z", *options],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
    )
    return [
        Path(os.fsdecode(value))
        for value in result.stdout.split(b"\0")
        if value
    ]


def ensure_no_local_artifacts_tracked() -> None:
    forbidden = [
        relative
        for relative in git_relative_files("--cached")
        if relative.as_posix() == LOCAL_PROFILE_NAME
        or any(
            part.casefold().endswith(".local") or ".local." in part.casefold()
            for part in relative.parts
        )
    ]
    if forbidden:
        formatted = ", ".join(path.as_posix() for path in forbidden)
        raise RuntimeError(
            "Git contiene perfiles o entregables reservados para uso local: "
            f"{formatted}. Retírelos del índice antes de publicar."
        )


def repository_files() -> Iterable[Path]:
    relative_files = git_relative_files(
        "--cached",
        "--others",
        "--exclude-standard",
    )
    for relative in relative_files:
        path = REPO_ROOT / relative
        if path.is_file():
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
    if suffix in ARCHIVE_SUFFIXES:
        if not zipfile.is_zipfile(path):
            yield "archivo", "FORMATO ZIP DAÑADO"
            return
        with zipfile.ZipFile(path) as archive:
            for member in archive.infolist():
                if member.is_dir():
                    continue
                yield "ruta interna ZIP", member.filename
                data = archive.read(member)
                inner_suffix = PurePosixPath(member.filename).suffix.lower()
                if inner_suffix in TEXT_SUFFIXES:
                    yield member.filename, decode_text(data)
                elif inner_suffix in OFFICE_SUFFIXES:
                    nested_stream = io.BytesIO(data)
                    if not zipfile.is_zipfile(nested_stream):
                        yield member.filename, "FORMATO OFFICE DAÑADO"
                        continue
                    nested_stream.seek(0)
                    with zipfile.ZipFile(nested_stream) as nested:
                        for inner_member in nested.infolist():
                            if inner_member.is_dir() or not inner_member.filename.lower().endswith(
                                (".xml", ".rels", ".txt")
                            ):
                                continue
                            visible_text, external_targets = xml_human_text(
                                nested.read(inner_member)
                            )
                            component = f"{member.filename}::{inner_member.filename}"
                            if visible_text:
                                yield component, visible_text
                            if external_targets:
                                yield f"{component} — relaciones externas", external_targets
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
    ensure_no_local_artifacts_tracked()
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
