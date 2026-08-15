# Informe de resolución — GA2-240202501-AA2-EV02

## Identificación

- **Producto evaluado:** video de presentación en inglés con diapositivas.
- **Sitio turístico elegido:** Cerro de Monserrate, Bogotá.
- **Aprendiz:** Jhon Steven Alvarez Ruiz.
- **Estado:** presentación, PDF y guion completos; grabación con la voz del aprendiz pendiente.

## Interpretación del instrumento

El documento suministrado es una lista de chequeo de dos páginas. Solicita presentar en inglés las características de un sitio turístico regional y apoyar el video con diapositivas que incluyan ubicación, elementos, descripción y opinión personal. El 30 % de la evaluación corresponde al uso oral del inglés y otro 30 % a pronunciación, fonología, ritmo y entonación.

El instrumento no fija ciudad, duración, número de diapositivas, formato de video ni aparición obligatoria en cámara. Como los archivos disponibles no identifican la ciudad del aprendiz, se tomó **Bogotá** como referencia regional y se eligió Monserrate por integrar naturaleza, cultura, religión, gastronomía y vista urbana.

## Cómo se resolvió

1. Se descompuso la rúbrica en contenido visual, contenido oral, pronunciación, estructura y entrega.
2. Se verificaron ubicación, altitud, accesos, elementos, longitud del sendero y recomendaciones mediante fuentes oficiales.
3. Se redactó un guion original de 493 palabras, nivel A2–B1 y duración objetivo aproximada de 4 minutos y 40 segundos.
4. Se diseñaron ocho diapositivas 16:9 con texto breve, fotografías reales y contraste suficiente.
5. Se creó un guion editable con tiempos, vocabulario visible, discurso completo, palabras difíciles, IPA y apoyo aproximado para hispanohablantes.
6. Se documentaron fuentes y licencias de las fotografías.
7. Se exportaron la presentación y el guion a PDF y se revisó visualmente cada diapositiva.

## Relación con la rúbrica

| Criterio | Peso | Evidencia preparada |
|---|---:|---|
| Características de un sitio turístico regional en inglés | 30 % | Las ocho diapositivas y el guion describen Monserrate completamente en inglés. |
| Ubicación, elementos, descripción y opinión | 20 % | Diapositivas 2, 3, 4 y 6 respectivamente. |
| Fonemas, ritmo, entonación y mensajes sencillos | 15 % | Guion segmentado por tiempo y tabla de pronunciación con IPA. Debe demostrarse con la voz del aprendiz. |
| Pronunciación clara y frases adecuadas | 15 % | Oraciones A2–B1 y lista de palabras para practicar. Debe demostrarse en la grabación. |
| Coherencia, cohesión y vocabulario | 5 % | Secuencia lineal: introducción, ubicación, elementos, descripción, actividades, opinión, recomendaciones y conclusión. |
| Estructura del video | 5 % | Storyboard de ocho secciones y tiempo objetivo 0:00–4:40. |
| Entrega dentro del plazo | 5 % | Depende del envío realizado por el aprendiz. |
| Envío por la plataforma oficial | 5 % | Depende del envío realizado por el aprendiz. |

## Entregables preparados

- [Presentación editable](03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pptx)
- [Presentación en PDF](03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pdf)
- [Guion oral editable](03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.docx)
- [Guion oral en PDF](03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.pdf)
- [Guion fuente](02_solucion/GUION_PRESENTACION.md)
- [Guía de grabación](02_solucion/GUIA_GRABACION.md)
- [Fuentes y créditos](02_solucion/FUENTES_Y_CREDITOS.md)
- [Código generador](02_solucion/generar_presentacion.py)
- [Instrumento original](01_enunciado/IE-GA2-240202501-AA2-EV02.pdf)

## Paso manual obligatorio

La rúbrica califica la pronunciación del aprendiz. Por esa razón no se entrega un video con voz sintética. Jhon Steven debe practicar con el guion, grabar su propia narración sobre las diapositivas, comprobar audio e imagen y subir el MP4 o enlace permitido a la plataforma oficial.

## Regeneración

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/02_solucion/requirements.txt
.venv/bin/python talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/02_solucion/generar_presentacion.py
libreoffice --headless --convert-to pdf --outdir talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Presentacion_Monserrate.pptx
libreoffice --headless --convert-to pdf --outdir talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega talleres/02-GA2-240202501-AA2-EV02-presentacion-monserrate/03_entrega/GA2-240202501-AA2-EV02_Guion_Oral.docx
```
