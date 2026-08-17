# Informe de resolución — GA3-220501093-AA2-EV01

## Identificación

- **Producto:** documento sobre fundamentos de programación estructurada y estructuras
  cíclicas.
- **Problemas resueltos:** cálculo de edad actual y determinación de año bisiesto.
- **Aprendiz:** Jhon Steven Alvarez Ruiz.
- **Estado:** completo, probado y verificado.

## Interpretación del instrumento

El PDF suministrado es una lista de chequeo de dos páginas. Sus tres indicadores exigen que
el análisis, el diseño y la implementación solucionen los problemas propuestos; que cada
algoritmo identifique entradas, salidas y procesos; y que el diseño se represente mediante
diagramas de flujo. Los indicadores son obligatorios y no incluyen una ponderación
porcentual.

Para precisar cuáles eran los problemas, el instrumento se contrastó con la
[guía de aprendizaje pública del mismo programa, proyecto, fase y evidencia](https://archivos.territorio.la/archivos/clases/Guianaprendizajen3nAct___7264160590b5042___.pdf),
página 5 del PDF. Allí se solicitan exactamente dos soluciones:

1. Calcular la edad actual en años a partir de la fecha de nacimiento y la fecha actual.
2. Determinar si un año ingresado es bisiesto.

La guía pide, para ambos casos, análisis de entradas, salidas y procesos, pseudocódigo y
diagrama de flujo. El producto es un solo documento, de extensión libre, en Word o PDF.

## Enfoque de solución

La entrega se diseñó como un documento técnico autocontenido de diez páginas. Cada problema
incluye definición, precondiciones, tabla de entradas–procesos–salidas, diccionario de datos,
pseudocódigo, diagrama de flujo y pruebas de escritorio. Una sección final relaciona las
estructuras secuenciales, condicionales y cíclicas con las instrucciones que las implementan.

Los algoritmos tienen ciclos de validación y reingreso de datos. Esta decisión hace visible
el uso real de estructuras cíclicas y evita calcular resultados con fechas inexistentes, una
fecha de nacimiento posterior o un año no positivo.

### Algoritmo 1: edad actual

- Recibe seis valores enteros: día, mes y año de nacimiento; día, mes y año actuales.
- Comprueba que ambas fechas existan en el calendario gregoriano y estén en orden
  cronológico.
- Calcula la diferencia entre los años y resta una unidad cuando el cumpleaños todavía no
  ha ocurrido en el año actual.
- Devuelve la edad en años completos.
- Para una persona nacida el 29 de febrero, en un año no bisiesto la edad aumenta al llegar
  el 1 de marzo; esta convención evita una interpretación implícita.

### Algoritmo 2: año bisiesto

- Recibe un año entero positivo.
- Calcula los residuos de la división entre 4, 100 y 400.
- Aplica la regla gregoriana completa: el año es bisiesto si es divisible por 400, o si es
  divisible por 4 y no por 100.
- Devuelve una respuesta afirmativa o negativa y permite analizar otro año.

La regla se verificó con la explicación del
[National Research Council Canada](https://nrc.canada.ca/en/certifications-evaluations-standards/canadas-official-time/what-years-are-leap-years).
Las fechas de prueba se escribieron como `YYYY-MM-DD`, siguiendo el orden del
[formato ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html), para evitar
ambigüedad.

## Verificación realizada

- Se ejecutaron **12 pruebas automatizadas**: siete para edad y cinco para año bisiesto.
- Las pruebas de edad cubren cumpleaños pendiente, exacto y cumplido; nacimiento en día
  bisiesto antes y después del aniversario adoptado; fecha inexistente y nacimiento posterior
  a la fecha actual.
- Las pruebas de bisiesto cubren un múltiplo de 400, un siglo no múltiplo de 400, un múltiplo
  de 4, un año común y un dato no positivo.
- Los pseudocódigos usan la notación documentada por
  [PSeInt](https://pseint.sourceforge.net/pseudocodigo.php). La lógica se comprobó mediante
  funciones de referencia ejecutables en el generador; no se afirma una ejecución directa en
  PSeInt porque esa aplicación no forma parte del entorno del repositorio.
- Se comprobaron la integridad del DOCX, las dos imágenes incrustadas, las diez páginas del
  PDF, la extracción completa del texto y la composición visual sin cortes ni desbordes.
- Las fechas incluidas son casos sintéticos y no corresponden a datos personales del
  aprendiz.

## Relación con la lista de chequeo

| Indicador del instrumento | Evidencia concreta en la entrega |
|---|---|
| El análisis, diseño e implementación solucionan los problemas propuestos | La sección 02 (páginas 3–6) desarrolla el cálculo de edad y la sección 03 (páginas 7–9) desarrolla la regla de año bisiesto; ambos producen el resultado solicitado. |
| Cada algoritmo registra entradas, salidas y procesos | Cada problema contiene una tabla de entradas–procesos–salidas, precondiciones y un diccionario de variables con tipo y propósito. |
| El diseño y la implementación utilizan diagramas de flujo | Las páginas 4 y 8 contienen diagramas independientes, con símbolos, decisiones `Sí/No`, ciclos de validación y ruta de terminación. |

## Correspondencia entre artefactos

| Componente | Cálculo de edad | Año bisiesto |
|---|---|---|
| Análisis | Página 3 | Página 7 |
| Diagrama de flujo | Página 4 | Página 8 |
| Pseudocódigo | Página 5 | Página 9 |
| Pruebas de escritorio | Página 6 | Página 9 |
| Fuente independiente | `01_calcular_edad.psc` | `02_determinar_anio_bisiesto.psc` |

## Archivos relacionados

- [Instrumento original](01_enunciado/IE-GA3-220501093-AA2-EV01.pdf)
- [Fuentes y referencias](02_solucion/FUENTES_Y_REFERENCIAS.md)
- [Pseudocódigo de edad](02_solucion/pseudocodigo/01_calcular_edad.psc)
- [Pseudocódigo de año bisiesto](02_solucion/pseudocodigo/02_determinar_anio_bisiesto.psc)
- [Diagrama de edad](02_solucion/recursos/diagramas/01_calcular_edad.png)
- [Diagrama de año bisiesto](02_solucion/recursos/diagramas/02_determinar_anio_bisiesto.png)
- [Código generador y pruebas](02_solucion/generar_entrega.py)
- [Versión editable](03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.docx)
- [PDF final](03_entrega/GA3-220501093-AA2-EV01_Fundamentos_Programacion_Estructurada.pdf)

## Regeneración

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r talleres/04-GA3-220501093-AA2-EV01-algoritmos-edad-bisiesto/02_solucion/requirements.txt
python3 automatizacion/resolver_evidencias.py resolver --taller 4
```
