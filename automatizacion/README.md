# Resolutor automático de evidencias

Este módulo convierte la solución de cada taller en un proceso reproducible. No inventa
respuestas para instrumentos desconocidos: registra los talleres ya analizados, ejecuta
sus generadores, crea los PDF, verifica los entregables y aplica una barrera de privacidad.

## Qué contiene

- Un catálogo de los siete talleres y sus productos esperados.
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
- Auditoría de texto, rutas, XML interno, archivos ZIP y metadatos de PDF, DOCX y PPTX.
- Detección de secuencias numéricas de alto riesgo, correos, claves privadas, tokens y
  valores confidenciales suministrados localmente.

## Uso

Ejecute los comandos desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py listar
python3 automatizacion/resolver_evidencias.py preparar
python3 automatizacion/resolver_evidencias.py resolver --todos
python3 automatizacion/resolver_evidencias.py validar --taller 7
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
- `04_entrega_personalizada.local` contiene exactamente un archivo identificado y listo
  para cargar en la plataforma SENA.

La edición local toma los datos de `perfil-aprendiz.local.json` y queda ignorada. La
auditoría falla si el perfil o cualquier componente de una ruta `.local` entra al índice,
incluso si se intentó agregarlo de manera forzada.

El quinto taller mantiene por compatibilidad su entrega personalizada anterior fuera del
repositorio. Los talleres sexto y séptimo ya usan el modelo de archivo local único y ningún
dato personal está codificado en sus generadores.

## Cómo agregar otro taller

1. Mantenga la estructura pública `01_enunciado`, `02_solucion`, `03_entrega` e informe.
2. Cree un generador determinista dentro de `02_solucion`.
3. Registre el generador, las exportaciones y los archivos esperados en `WORKSHOPS`.
4. Si se requiere identificación, genere un solo producto dentro de
   `04_entrega_personalizada.local`.
5. Ejecute `resolver` y corrija cualquier fallo antes de publicar.

La automatización reduce errores repetitivos, pero la revisión académica sigue siendo
necesaria. En particular, una evidencia que evalúe la voz del aprendiz debe conservar su
paso de grabación personal.

## Control en GitHub

El flujo `.github/workflows/verificar-evidencias.yml` ejecuta la validación de integridad y
la auditoría de privacidad en cada envío y solicitud de cambios. La publicación queda así
protegida por los mismos controles que se pueden ejecutar localmente.
