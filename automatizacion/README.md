# Resolutor automático de evidencias

Este módulo convierte la solución de cada taller en un proceso reproducible. No inventa
respuestas para instrumentos desconocidos: registra los talleres ya analizados, ejecuta
sus generadores, crea los PDF, verifica los entregables y aplica una barrera de privacidad.

La selección de formato es deliberada: los documentos simples permanecen como PDF y solo
se genera un ZIP cuando la guía pide un paquete o la solución necesita conservar varios
archivos ejecutables o fuentes. Nunca se crea un ZIP para envolver uno o varios PDF.

## Qué contiene

- Un catálogo de los ocho talleres y sus productos esperados.
- Preparación opcional del entorno Python.
- Ejecución de los generadores incluidos en cada carpeta `02_solucion`.
- Exportación atómica de DOCX y PPTX a PDF mediante LibreOffice.
- Comprobación de integridad de archivos Office y cantidad de páginas de cada PDF.
- Control de las 200–400 palabras, Arial 12 e interlineado 1,5 exigidos en el tercer taller.
- Comprobación de las diez páginas y los dos diagramas incrustados del cuarto taller.
- Comprobación de 33 páginas, diez diagramas, autor genérico y manifiesto ZIP exacto en el
  quinto taller.
- Comprobación de doce páginas, cuatro figuras, autor genérico y secciones obligatorias en
  el sexto taller.
- Comprobación del manifiesto ZIP, las cuatro fuentes JavaScript y la suite de pruebas del
  séptimo taller.
- Comprobación de los dos PDF públicos, sus metadatos genéricos y los contenidos
  obligatorios del guion y la guía de pronunciación del octavo taller.
- Auditoría de texto, rutas, XML interno, archivos ZIP y metadatos de PDF, DOCX y PPTX.
- Detección de secuencias numéricas de alto riesgo, correos, claves privadas, tokens y
  valores confidenciales suministrados localmente.

## Uso

Ejecute los comandos desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py listar
python3 automatizacion/resolver_evidencias.py preparar
python3 automatizacion/resolver_evidencias.py resolver --todos
python3 automatizacion/resolver_evidencias.py validar --taller 8
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

## Entregas personalizadas locales

El modelo vigente asigna funciones inequívocas a dos directorios:

- `03_entrega` contiene exclusivamente los productos públicos de GitHub.
- `04_entrega_personalizada.local` contiene solo los documentos identificados definidos
  para esa evidencia; nunca contiene copias públicas.

La edición local toma los datos de `perfil-aprendiz.local.json` y queda ignorada. La
auditoría falla si el perfil o cualquier componente de una ruta `.local` entra al índice,
incluso si se intentó agregarlo de manera forzada.

El quinto taller mantiene por compatibilidad su entrega personalizada anterior fuera del
repositorio. Los talleres sexto y séptimo usan un único archivo local. El octavo conserva
dos documentos locales con funciones inequívocas: `ENTREGAR_...` es el guion con enlace
que se carga en la plataforma y `APOYO_GRABACION_...` sirve solo para practicar la
pronunciación. Ningún dato personal está codificado en los generadores.

## Cómo agregar otro taller

1. Mantenga la estructura pública `01_enunciado`, `02_solucion`, `03_entrega` e informe.
2. Cree un generador determinista dentro de `02_solucion`.
3. Registre el generador, las exportaciones y los archivos esperados en `WORKSHOPS`.
4. Si se requiere identificación, genere únicamente los productos personalizados que la
   evidencia necesita dentro de `04_entrega_personalizada.local`, con nombres que indiquen
   sin ambigüedad cuál se entrega y cuál es solo apoyo.
5. Ejecute `resolver` y corrija cualquier fallo antes de publicar.

La automatización reduce errores repetitivos, pero la revisión académica sigue siendo
necesaria. En particular, una evidencia que evalúe la voz del aprendiz debe conservar su
paso de grabación personal.

## Control en GitHub

El flujo `.github/workflows/verificar-evidencias.yml` ejecuta la validación de integridad y
la auditoría de privacidad en cada envío y solicitud de cambios. La publicación queda así
protegida por los mismos controles que se pueden ejecutar localmente.
