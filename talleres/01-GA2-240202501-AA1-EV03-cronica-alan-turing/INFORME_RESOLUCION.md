# Informe de resolución — GA2-240202501-AA1-EV03

## Identificación

- **Producto:** crónica en inglés.
- **Tema elegido:** Alan Turing y su relación con la computación moderna.
- **Aprendiz:** Jhon Steven Alvarez Ruiz.
- **Estado:** completo y verificado.

## Interpretación del instrumento

El PDF suministrado es una lista de chequeo, no la guía completa. Exige una crónica sobre un personaje icónico, redactada principalmente en pasado simple, con vocabulario de apariencia, comportamiento y personalidad, ideas cronológicas, opinión personal y una relación explícita con Análisis y Desarrollo de Software.

El instrumento no determina personaje, extensión, número de páginas, portada, imágenes ni norma de citación. Se eligió a Alan Turing porque sus aportes permiten relacionar de forma directa el análisis de problemas, los algoritmos, la programación, las pruebas y el trabajo colaborativo con el área de formación.

## Cómo se resolvió

1. Se extrajeron los ocho criterios de la rúbrica y sus pesos.
2. Se construyó una secuencia cronológica: primeros años, máquina teórica, Bletchley Park, ACE, prueba de Turing, injusticia y legado.
3. Se redactó una crónica original de 621 palabras, con predominio del pasado simple y una conclusión en presente sobre su legado.
4. Se incluyeron rasgos de apariencia, comportamiento y personalidad dentro de la narración.
5. Se verificó que Turing no fuera presentado como autor de Colossus ni como la única persona que descifró Enigma.
6. Se diseñó una entrega de tres páginas en tamaño carta y se exportó a DOCX y PDF.
7. Se revisaron ortografía, integridad del DOCX, metadatos, número de páginas y cortes visuales del PDF.

## Relación con la rúbrica

| Criterio | Peso | Evidencia en la solución |
|---|---:|---|
| Crónica bien estructurada y con léxico adecuado | 30 % | Ocho secciones cronológicas y formato editorial legible. |
| Inglés y pasado simple | 15 % | Verbos como *was, studied, published, designed, worked, developed* y *died*. |
| Apariencia, comportamiento, personalidad y punto de vista | 15 % | Descripción física, hábitos, rasgos personales y expresiones como *In my view* e *I believe*. |
| Estrategias para textos sencillos | 5 % | Oraciones breves, conectores temporales y una idea central por párrafo. |
| Secuencia, puntuación y gramática | 10 % | Línea de tiempo desde 1912 hasta el legado actual. |
| Relación con el área de formación | 15 % | Análisis, diseño, instrucciones, pruebas, mejora, programación y colaboración. |
| Cohesión de párrafos | 5 % | Secciones enlazadas por fechas y etapas profesionales. |
| Ortografía y lectura fluida | 5 % | Revisión ortográfica y exportación visual comprobada. |

## Archivos relacionados

- [Instrumento original](01_enunciado/IE-GA2-240202501-AA1-EV03.pdf)
- [Código generador](02_solucion/generar_entrega.py)
- [Versión editable](03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.docx)
- [PDF final](03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.pdf)
- [Texto plano](03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.txt)

## Regeneración

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/02_solucion/requirements.txt
.venv/bin/python talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/02_solucion/generar_entrega.py
libreoffice --headless --convert-to pdf --outdir talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/03_entrega talleres/01-GA2-240202501-AA1-EV03-cronica-alan-turing/03_entrega/GA2-240202501-AA1-EV03_Cronica_Alan_Turing.docx
```
