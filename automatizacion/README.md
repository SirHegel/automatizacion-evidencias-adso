# Resolutor automático de evidencias

Este módulo convierte la solución de cada taller en un proceso reproducible. No inventa
respuestas para instrumentos desconocidos: registra los talleres ya analizados, ejecuta
sus generadores, crea los PDF, verifica los entregables y aplica una barrera de privacidad.

## Qué contiene

- Un catálogo de los cuatro talleres y sus productos esperados.
- Preparación opcional del entorno Python.
- Ejecución de los generadores incluidos en cada carpeta `02_solucion`.
- Exportación atómica de DOCX y PPTX a PDF mediante LibreOffice.
- Comprobación de integridad de archivos Office y cantidad de páginas de cada PDF.
- Control de las 200–400 palabras, Arial 12 e interlineado 1,5 exigidos en el tercer taller.
- Comprobación de las diez páginas y los dos diagramas incrustados del cuarto taller.
- Auditoría de texto, rutas, XML interno y metadatos de PDF, DOCX y PPTX.
- Detección de secuencias numéricas de alto riesgo, correos, claves privadas, tokens y
  valores confidenciales suministrados localmente.

## Uso

Ejecute los comandos desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py listar
python3 automatizacion/resolver_evidencias.py preparar
python3 automatizacion/resolver_evidencias.py resolver --todos
python3 automatizacion/resolver_evidencias.py validar --taller 4
python3 automatizacion/resolver_evidencias.py auditar
```

`resolver --todos` sigue esta secuencia:

1. Ejecuta el generador de cada taller.
2. Exporta los documentos editables a PDF.
3. Comprueba que todos los productos existan, no estén vacíos y se puedan abrir.
4. Audita el repositorio completo.
5. Finaliza con error si cualquier control falla.

## Lista privada opcional

Para comprobar valores confidenciales concretos sin publicarlos en Git, cree el archivo
`.privacidad.local` en la raíz, con un valor por línea, y ejecute:

```bash
python3 automatizacion/resolver_evidencias.py auditar
```

Ese archivo está excluido mediante `.gitignore`. También se puede indicar otra ruta con
`--lista-privada`. Nunca se deben guardar identificadores ni credenciales dentro del código.

## Cómo agregar otro taller

1. Mantenga la estructura `01_enunciado`, `02_solucion`, `03_entrega` e informe.
2. Cree un generador determinista dentro de `02_solucion`.
3. Registre el generador, las exportaciones y los archivos esperados en `WORKSHOPS`.
4. Ejecute `resolver` y corrija cualquier fallo antes de publicar.

La automatización reduce errores repetitivos, pero la revisión académica sigue siendo
necesaria. En particular, una evidencia que evalúe la voz del aprendiz debe conservar su
paso de grabación personal.

## Control en GitHub

El flujo `.github/workflows/verificar-evidencias.yml` ejecuta la validación de integridad y
la auditoría de privacidad en cada envío y solicitud de cambios. La publicación queda así
protegida por los mismos controles que se pueden ejecutar localmente.
