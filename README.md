# Evidencias SENA — Inglés

Repositorio organizado por taller para **Jhon Steven Alvarez Ruiz**.

Cada evidencia es autocontenida: el instrumento original, la explicación de cómo se resolvió y los archivos finales permanecen dentro de la misma carpeta.

## Estructura

```text
├── talleres/
│   ├── 01-GA2-240202501-AA1-EV03-cronica-alan-turing/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   └── 02-GA2-240202501-AA2-EV02-presentacion-monserrate/
│       ├── 01_enunciado/
│       ├── 02_solucion/
│       ├── 03_entrega/
│       └── INFORME_RESOLUCION.md
└── automatizacion/
    ├── resolver_evidencias.py
    └── README.md
```

Las carpetas siguen siempre el mismo orden:

1. `01_enunciado`: documento original que define la evidencia.
2. `02_solucion`: guiones, fuentes, recursos y código utilizado para resolverla.
3. `03_entrega`: archivos finales editables y exportados.
4. `INFORME_RESOLUCION.md`: relación entre la rúbrica y la solución realizada.

La carpeta `automatizacion` contiene el resolutor que regenera las entregas existentes,
comprueba su integridad y detiene el proceso si detecta datos personales no autorizados.

## Talleres

| N.º | Evidencia | Producto | Estado | Informe | Entrega principal |
|---:|---|---|---|---|---|
| 1 | GA2-240202501-AA1-EV03 | Crónica en inglés sobre Alan Turing | Completo | [Ver informe](talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/INFORME_RESOLUCION.md) | [PDF](talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.pdf) · [DOCX](talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.docx) |
| 2 | GA2-240202501-AA2-EV02 | Presentación en inglés sobre Monserrate | Presentación lista; grabación personal pendiente | [Ver informe](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/INFORME_RESOLUCION.md) | [PPTX](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pptx) · [PDF](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pdf) · [Guion](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.pdf) |

## Estado del segundo taller

La presentación de ocho diapositivas, su versión PDF y el guion oral con apoyo de pronunciación están completos. El video no se genera con una voz artificial: debe grabarlo el aprendiz con su propia voz, porque el instrumento evalúa pronunciación, ritmo y entonación.

## Resolución y auditoría automáticas

Desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py listar
python3 automatizacion/resolver_evidencias.py resolver --todos
python3 automatizacion/resolver_evidencias.py auditar
```

El comando `resolver` ejecuta los generadores documentados, exporta los formatos PDF y
valida los entregables. El comando `auditar` inspecciona archivos de texto, PDF, DOCX y
PPTX; devuelve un código de error si encuentra identificadores personales prohibidos.
