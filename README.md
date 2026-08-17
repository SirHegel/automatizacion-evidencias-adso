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
│   └── 05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/
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
| 3 | GA2-240202501-AA2-EV03 | Correo en inglés de solicitud de empleo | Completo | [Ver informe](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/INFORME_RESOLUCION.md) | [PDF](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.pdf) · [DOCX](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.docx) · [TXT](talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.txt) |
| 4 | GA3-220501093-AA2-EV01 | Algoritmos de edad y año bisiesto | Completo | [Ver informe](talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/INFORME_RESOLUCION.md) | [PDF](talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.pdf) · [DOCX](talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.docx) |
| 5 | GA3-220501093-AA2-EV03 | Funciones y procedimientos en algoritmos | Completo; versión pública anonimizada | [Ver informe](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/INFORME_RESOLUCION.md) | [ZIP](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.zip) · [PDF](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.pdf) · [DOCX](talleres/05-GA3-220501093-AA2-EV03-funciones-procedimientos-algoritmos/03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.docx) |

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

## Resolución y auditoría automáticas

Desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py listar
python3 automatizacion/resolver_evidencias.py resolver --todos
python3 automatizacion/resolver_evidencias.py auditar
```

El comando `resolver` ejecuta los generadores documentados, exporta los formatos PDF y
valida los entregables. El comando `auditar` inspecciona archivos de texto, PDF, DOCX, PPTX
y el contenido textual de los ZIP; devuelve un código de error si encuentra datos prohibidos.
