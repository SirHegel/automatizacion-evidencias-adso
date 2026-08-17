# Automatización de evidencias SENA — Análisis y Desarrollo de Software

Sistema reproducible para organizar, resolver, generar y validar talleres del programa de
Análisis y Desarrollo de Software.

Cada evidencia es autocontenida: el instrumento original, la explicación de cómo se resolvió y los archivos finales permanecen dentro de la misma carpeta.

## Estructura

```text
├── talleres/
│   ├── 01-GA2-240202501-AA1-EV03-cronica-alan-turing/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   ├── 02-GA2-240202501-AA2-EV02-presentacion-monserrate/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   ├── 03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   ├── 04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   ├── 05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   ├── 06-GA3-220501093-AA3-EV01-bases-teoricas-javascript/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   ├── 07-GA3-220501093-AA3-EV02-estructuras-almacenamiento-javascript/
│   │   ├── 01_enunciado/
│   │   ├── 02_solucion/
│   │   ├── 03_entrega/
│   │   └── INFORME_RESOLUCION.md
│   └── 08-GA3-240202501-AA1-EV02-audio-obligaciones-laborales-ingles/
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
3. `03_entrega`: productos públicos sin datos personales, destinados a GitHub.
4. `04_entrega_personalizada.local`: únicamente los documentos identificados que se usan
   para entregar o grabar la evidencia; Git los ignora por contener datos sensibles.
5. `INFORME_RESOLUCION.md`: relación entre la rúbrica y la solución realizada.

La carpeta `automatizacion` contiene el resolutor que regenera las entregas existentes,
comprueba su integridad y detiene el proceso si detecta datos personales no autorizados.

El formato sigue la naturaleza de cada evidencia: un documento se publica y entrega como
PDF; un ZIP se usa únicamente cuando la guía exige un paquete o cuando deben conservarse
varios archivos funcionales, como código o una aplicación. Los PDF sencillos no se
empaquetan en ZIP.

## Talleres

| N.º | Evidencia | Producto | Estado | Informe | Entrega principal |
|---:|---|---|---|---|---|
| 1 | GA2-240202501-AA1-EV03 | Crónica en inglés sobre Alan Turing | Completo | [Ver informe](talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/INFORME_RESOLUCION.md) | [PDF](talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.pdf) · [DOCX](talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.docx) |
| 2 | GA2-240202501-AA2-EV02 | Presentación en inglés sobre Monserrate | Presentación lista; grabación personal pendiente | [Ver informe](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/INFORME_RESOLUCION.md) | [PPTX](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pptx) · [PDF](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pdf) · [Guion](talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.pdf) |
| 3 | GA2-240202501-AA2-EV03 | Correo en inglés de solicitud de empleo | Completo | [Ver informe](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/INFORME_RESOLUCION.md) | [PDF](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.pdf) · [DOCX](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.docx) · [TXT](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.txt) |
| 4 | GA3-220501093-AA2-EV01 | Algoritmos de edad y año bisiesto | Completo | [Ver informe](talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/INFORME_RESOLUCION.md) | [PDF](talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.pdf) · [DOCX](talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.docx) |
| 5 | GA3-220501093-AA2-EV03 | Funciones y procedimientos en algoritmos | Completo; versión pública anonimizada | [Ver informe](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/INFORME_RESOLUCION.md) | [ZIP](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.zip) · [PDF](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.pdf) · [DOCX](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.docx) |
| 6 | GA3-220501093-AA3-EV01 | Bases teóricas de estructuras de almacenamiento en memoria | Completo; publicación saneada y un único PDF local para SENA | [Ver informe](talleres/06-GA3-220501093-AA3-EV01-bases-teoricas-javascript/INFORME_RESOLUCION.md) | [PDF](talleres/06-GA3-220501093-AA3-EV01-bases-teoricas-javascript/03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.pdf) · [DOCX](talleres/06-GA3-220501093-AA3-EV01-bases-teoricas-javascript/03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.docx) |
| 7 | GA3-220501093-AA3-EV02 | Problemas algorítmicos con estructuras de almacenamiento | Completo; cuatro programas probados y un único ZIP local para SENA | [Ver informe](talleres/07-GA3-220501093-AA3-EV02-estructuras-almacenamiento-javascript/INFORME_RESOLUCION.md) | [ZIP público](talleres/07-GA3-220501093-AA3-EV02-estructuras-almacenamiento-javascript/03_entrega/GA3-220501093-AA3-EV02_Soluciones_JavaScript_PUBLICO.zip) |
| 8 | GA3-240202501-AA1-EV02 | Audio en inglés sobre obligaciones laborales y académicas | Guion y pronunciación listos; grabación, enlace y dos datos por completar | [Ver informe](talleres/08-GA3-240202501-AA1-EV02-audio-obligaciones-laborales-ingles/INFORME_RESOLUCION.md) | [Guion público](talleres/08-GA3-240202501-AA1-EV02-audio-obligaciones-laborales-ingles/03_entrega/GA3-240202501-AA1-EV02_Guion_Audio_PUBLICO.pdf) · [Pronunciación pública](talleres/08-GA3-240202501-AA1-EV02-audio-obligaciones-laborales-ingles/03_entrega/GA3-240202501-AA1-EV02_Guia_Pronunciacion_PUBLICO.pdf) |

## Estado del segundo taller

La presentación de ocho diapositivas, su versión PDF y el guion oral con apoyo de pronunciación están completos. El video no se genera con una voz artificial: debe grabarlo el aprendiz con su propia voz, porque el instrumento evalúa pronunciación, ritmo y entonación.

## Estado del tercer taller

El correo de postulación laboral está completo en TXT, DOCX y PDF. La entrega tiene 268
palabras, ocupa una página y conserva Arial 12 e interlineado 1,5. La versión pública no
incluye datos de contacto sensibles; indica que el destinatario puede responder al mensaje.

## Estado del cuarto taller

El documento técnico está completo en DOCX y PDF. Desarrolla el análisis, diseño e
implementación de dos algoritmos: cálculo de edad en años cumplidos y validación de año
bisiesto. Incluye tablas de entradas–procesos–salidas, diccionarios de datos, pseudocódigo,
dos diagramas de flujo y 12 pruebas automatizadas con casos válidos y erróneos.

## Estado del quinto taller

El taller está completo en ZIP, DOCX y PDF. Resuelve diez problemas mediante funciones o
procedimientos, con diez pseudocódigos, diez diagramas y 34 comprobaciones automáticas. La
publicación está anonimizada; la entrega personalizada se conserva fuera del repositorio.

## Estado del sexto taller

El documento está completo en DOCX y PDF. En doce páginas desarrolla los cuatro temas de
la lista de chequeo, incluye ejemplos de JavaScript, cuatro figuras originales, conclusiones,
matriz de cumplimiento y referencias. `03_entrega` conserva solo la edición pública. La
carpeta ignorada `04_entrega_personalizada.local` contiene exactamente un PDF identificado:
es el único archivo que se debe seleccionar para entregar esta evidencia al SENA.

## Estado del séptimo taller

El taller resuelve en JavaScript los cuatro problemas de la guía: figuras planas, análisis
de diez edades, mezcla de vectores ascendentes y encuesta musical persistente. Incluye
validación de entradas, funciones reutilizables, administración JSON y pruebas automáticas.
No es un sistema integrado: son cuatro programas y el cuarto funciona como miniaplicación
con menú, operaciones de gestión y almacenamiento en archivo.
GitHub recibe únicamente el ZIP público; `04_entrega_personalizada.local` contiene un solo
ZIP con el nombre y los datos del aprendiz, listo para cargar en la plataforma.

## Estado del octavo taller

El guion en inglés cubre una presentación breve y una opinión sobre actitudes, creencias y
obligaciones en contextos académico y laboral. Emplea de forma explícita `have to`, `must`
y `should` con verbo base. También existe una guía paralela de pronunciación, pausas,
acentos, ritmo y entonación para apoyar una grabación de dos a cinco minutos.

GitHub conserva dos PDF públicos saneados y separados por nombre: el guion y la guía de
pronunciación. Localmente,
`04_entrega_personalizada.local` contiene solo dos documentos identificados: el archivo
`ENTREGAR_...` que recibirá el enlace reproducible del audio y el archivo
`APOYO_GRABACION_...`, marcado de manera visible como apoyo que no se debe subir. La
grabación debe hacerse con la voz real del aprendiz; no se genera una voz artificial.

## Resolución y auditoría automáticas

Desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py listar
python3 automatizacion/resolver_evidencias.py resolver --todos
python3 automatizacion/resolver_evidencias.py auditar
```

El comando `resolver` ejecuta los generadores documentados, exporta los formatos PDF y
valida los entregables. El comando `auditar` inspecciona archivos de texto, JavaScript, PDF,
DOCX, PPTX y el contenido textual de los ZIP; devuelve un código de error si encuentra datos
prohibidos.
