# Informe de resolución — GA2-240202501-AA2-EV03

## Identificación

- **Producto:** documento escrito en inglés con formato de correo electrónico.
- **Cargo elegido:** Junior Software Developer.
- **Aprendiz:** Jhon Steven Alvarez Ruiz.
- **Estado:** completo y verificado.

## Interpretación del instrumento

El PDF suministrado es una lista de chequeo de dos páginas, no la guía completa. Evalúa la
estructura del correo, el léxico, la gramática básica, la expresión de puntos de vista, la
Netiqueta, la correspondencia con el perfil profesional, la cohesión y la legibilidad.

Para no completar los aspectos faltantes por intuición, se contrastó el instrumento con una
[guía pública de otro programa SENA que incorpora la misma competencia transversal y evidencia](https://archivos.territorio.la/archivos/clases/Guianaprendizajen2___806557cf257e5ce___.pdf).
La guía solicita entre 200 y 400 palabras, una extensión de 1 a 3 páginas y entrega en Word y
PDF. También exige asunto descriptivo, saludo, propósito, cargo, habilidades, aporte a la
empresa, contacto, despedida, nombre, lugar de origen y profesión. Se aplicó el lineamiento
de entrega de Arial 12 e interlineado 1,5.

## Decisiones de contenido

- Se eligió **Junior Software Developer** por su relación directa con el programa de
  formación.
- El destinatario es **Hiring Manager** porque el instrumento no especifica empresa ni
  persona responsable.
- El perfil se presenta honestamente como aprendiz en formación; no se inventaron empleos,
  títulos obtenidos ni dominio avanzado de herramientas.
- El mensaje ofrece un canal de respuesta mediante el propio correo, sin publicar teléfono
  ni dirección electrónica en el repositorio.
- Se indicó **Colombia** como lugar de origen y se evitó atribuir una ciudad no confirmada.

## Cómo se resolvió

1. Se descompusieron los ocho indicadores y los requisitos estructurales de la guía.
2. Se redactó un correo original de 268 palabras, con nivel A2–B1 y una secuencia lineal:
   propósito, formación, habilidades, cualidades, aporte, planes, contacto y cierre.
3. Se combinaron presente, experiencias de formación, opinión y planes futuros mediante
   estructuras sencillas y comprensibles.
4. Se diseñó una página tamaño carta que representa un correo real con campos *From*, *To*
   y *Subject*, manteniendo Arial 12 e interlineado 1,5 en todo el texto visible.
5. Se generaron las versiones TXT y DOCX desde una única fuente y se exportó el PDF.
6. Se comprobaron el conteo de palabras, la integridad del DOCX, la tipografía, el tamaño,
   el interlineado, la página única, la extracción completa de texto y la composición visual.
7. Se aplicó la auditoría de privacidad del repositorio a los archivos fuente y finales.

## Relación con la rúbrica

| Criterio | Peso | Evidencia en la solución |
|---|---:|---|
| Correo estructurado, léxico, ortografía, puntuación y formato | 30 % | Encabezado de tres campos, saludo, siete párrafos breves, cierre y firma formal. |
| Control gramatical y estructuras básicas del inglés | 15 % | Presente, presente perfecto, modales, condicional con *if* y futuro con *will*. |
| Descripciones y punto de vista sobre la postulación | 15 % | Describe formación, habilidades y cualidades; expresa opinión sobre el software útil. |
| Estrategias para redactar textos sencillos | 5 % | Una idea central por párrafo y vocabulario A2–B1. |
| Netiqueta, puntuación y gramática | 10 % | Asunto preciso, tratamiento respetuoso, tono constante, agradecimiento y despedida. |
| Solicitud acorde con el perfil profesional | 15 % | Postulación a desarrollo de software vinculada con análisis, lógica, bases de datos, pruebas, documentación y Git. |
| Cohesión y coherencia | 5 % | Avanza desde el propósito hasta la disponibilidad para entrevista sin apartarse del cargo. |
| Ortografía y lectura fluida | 5 % | Revisión lingüística y PDF de una página sin cortes ni texto desbordado. |

## Cumplimiento de la estructura solicitada

| Elemento | Ubicación |
|---|---|
| Asunto descriptivo | *Application for the Junior Software Developer Position*. |
| Saludo | *Dear Hiring Manager* y saludo cordial inicial. |
| Propósito y cargo | Primera sección del cuerpo: presentación de la postulación y cargo. |
| Habilidades | Segundo párrafo del cuerpo. |
| Aporte a la empresa y punto de vista | Tercer párrafo del cuerpo. |
| Interés y planes | Cuarto párrafo del cuerpo. |
| Contacto | Quinto párrafo: respuesta directa al mensaje. |
| Despedida y remitente | Agradecimiento, *Sincerely*, nombre, país y perfil profesional. |

## Archivos relacionados

- [Instrumento original](01_enunciado/IE-GA2-240202501-AA2-EV03.pdf)
- [Texto fuente](02_solucion/TEXTO_CORREO.txt)
- [Código generador](02_solucion/generar_entrega.py)
- [Versión editable](03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.docx)
- [PDF final](03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.pdf)
- [Texto plano](03_entrega/GA2-240202501-AA2-EV03_Correo_Solicitud_Empleo.txt)

## Regeneración

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r talleres/03-GA2-240202501-AA2-EV03-correo-solicitud-empleo/02_solucion/requirements.txt
python3 automatizacion/resolver_evidencias.py resolver --taller 3
```
