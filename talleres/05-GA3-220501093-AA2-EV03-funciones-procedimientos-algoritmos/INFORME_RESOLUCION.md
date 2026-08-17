# Informe público de resolución — GA3-220501093-AA2-EV03

## Estado

- **Producto:** taller de funciones y procedimientos en la solución de algoritmos.
- **Cobertura:** diez problemas, diez pseudocódigos y diez diagramas de flujo.
- **Formato de entrega:** DOCX, PDF y paquete ZIP.
- **Privacidad:** versión pública anonimizada; el informe personalizado se mantiene fuera
  del repositorio.
- **Estado:** completo, probado y verificado.

## Interpretación del instrumento

El instrumento suministrado contiene veinte indicadores binarios. Para cada problema, uno
exige una solución coherente mediante diagrama de flujo y otro exige una solución coherente
mediante pseudocódigo. No establece porcentajes ni permite sustituir una notación por la otra.

El instrumento no incluye los enunciados. Para obtenerlos se consultó la
[guía de aprendizaje correspondiente](https://archivos.territorio.la/archivos/clases/Guianaprendizajen3nAct___7264160590b5042___.pdf),
páginas 5 y 6 del PDF. La guía solicita considerar estructuras secuenciales, condicionales y
repetitivas, resolver cada problema con ambas notaciones y entregar un único archivo ZIP con
todas las soluciones.

También se utilizó el
[material formativo oficial sobre análisis y solución de problemas mediante algoritmos](https://zajuna.sena.edu.co/Repositorio/Titulada/institution/SENA/Tecnologia/228118/Contenido/OVA/CF13/index.html)
y la [documentación de subprocesos de PSeInt](https://pseint.sourceforge.net/index.php?cual=Subprocesos&mode=estricto&page=ejemplos.php).

## Diseño general

Cada problema se desarrolló en tres páginas:

1. Análisis: enunciado, entradas, proceso, salida, variables, restricciones y pruebas.
2. Diseño: diagrama de flujo con validaciones, decisiones y ciclos visibles.
3. Implementación: pseudocódigo completo con proceso principal y módulos reutilizables.

La entrega tiene 33 páginas: portada pública, metodología, treinta páginas de desarrollo y
una matriz final que permite comprobar los veinte indicadores.

## Soluciones construidas

| N.º | Problema | Módulo principal | Regla central |
|---:|---|---|---|
| 1 | Ritmo de una maratón | `CalcularRitmoMinutosPorKilometro` | Convertir 2 h 25 min a 145 min y dividir entre 42,195 km. |
| 2 | Celsius a Fahrenheit | `ConvertirCelsiusAFahrenheit` | `F = (9/5)C + 32`. |
| 3 | Nota del primer parcial | `CalcularNotaPrimerParcial` | Promedio de dos talleres y cuestionario al 30 %; examen al 70 %. |
| 4 | Duplicación de capital | `CalcularDuplicacion` | Capitalización compuesta anual hasta alcanzar al menos el doble. |
| 5 | Veinte números menores o iguales a 25 | `EsMenorOIgualAlLimite` | Evaluar exactamente veinte entradas y mostrar las que cumplen. |
| 6 | Venta de cinco camisas | `ConvertirDolaresAPesos` | Sumar cinco precios en dólares y aplicar una tasa positiva ingresada. |
| 7 | Consumos de restaurante | `CalcularPago` | Descontar 20 % solo cuando el consumo sea mayor que 50000. |
| 8 | Hora del siguiente segundo | `AvanzarUnSegundo` | Propagar cambios de segundo a minuto, hora y día. |
| 9 | Producto desde 1 hasta N | `CalcularProductoUnoHastaN` | Acumular el producto; aceptar `0! = 1`. |
| 10 | Tabla de multiplicar decreciente | `MostrarTablaDecreciente` | Recorrer los multiplicadores desde 10 hasta 1. |

## Decisiones frente a ambigüedades

- Se adoptó la escala de notas de 0 a 5 y se dio el mismo peso a las tres actividades que
  conforman el componente del 30 %.
- El problema financiero se resolvió con interés compuesto anual. Capital y tasa deben ser
  positivos, y el resultado es el primer año entero que alcanza la meta.
- La tasa entre dólares y pesos se solicita como entrada para no incorporar un valor que
  cambia con el tiempo.
- La cantidad de clientes del restaurante se solicita antes del ciclo. Un consumo exactamente
  igual a 50000 no recibe descuento porque el enunciado indica que debe exceder ese valor.
- El producto desde 1 hasta N se interpreta como factorial para enteros no negativos.

## Verificación

El generador contiene implementaciones de referencia independientes del pseudocódigo. Se
ejecutaron **34 comprobaciones automáticas** que cubren:

- resultados normales de los diez problemas;
- valores frontera como 25, 50000, `0!` y `23:59:59`;
- rechazo de distancias, tasas, notas, horas y cantidades fuera del dominio;
- ciclos con cantidad exacta de entradas;
- propagación de cambios de minuto, hora y día;
- equivalencia entre conversiones y resultados esperados.

PSeInt no está instalado en el entorno de generación. Por ello no se afirma una ejecución
directa allí: la sintaxis fue revisada estructuralmente según su documentación y la lógica se
comprobó con las implementaciones de referencia ejecutables.

Además, se validan automáticamente:

- las 33 páginas del PDF;
- los diez diagramas incrustados en el DOCX;
- los 22 archivos exactos del ZIP público;
- la equivalencia entre el DOCX externo y el incluido en el ZIP;
- la ausencia de macros, objetos incrustados y rutas inseguras;
- el autor público genérico en los metadatos DOCX y PDF;
- el texto de los pseudocódigos y del DOCX incluido dentro del ZIP.

## Cobertura de la lista de chequeo

| Problema | Diagrama | Pseudocódigo | Indicadores cubiertos |
|---:|---|---|---:|
| 1 | Página 4 | Página 5 | 1–2 |
| 2 | Página 7 | Página 8 | 3–4 |
| 3 | Página 10 | Página 11 | 5–6 |
| 4 | Página 13 | Página 14 | 7–8 |
| 5 | Página 16 | Página 17 | 9–10 |
| 6 | Página 19 | Página 20 | 11–12 |
| 7 | Página 22 | Página 23 | 13–14 |
| 8 | Página 25 | Página 26 | 15–16 |
| 9 | Página 28 | Página 29 | 17–18 |
| 10 | Página 31 | Página 32 | 19–20 |

## Separación de privacidad

La versión pública no contiene nombre, contacto, número de grupo, instructor, centro, ciudad,
dirección ni firma del aprendiz. Su portada y sus metadatos utilizan una identidad académica
genérica.

La variante personalizada se genera mediante un perfil externo y se guarda en una carpeta
que está fuera del repositorio. El generador rechaza cualquier intento de usar como perfil o
destino privado una ruta ubicada dentro del proyecto. De esta manera, una operación amplia de
Git no puede incluir accidentalmente el informe privado.

## Archivos públicos

- [Instrumento original](01_enunciado/IE-GA3-220501093-AA2-EV03.pdf)
- [Fuentes y decisiones](02_solucion/FUENTES_Y_REFERENCIAS.md)
- [Generador y pruebas](02_solucion/generar_entrega.py)
- [Pseudocódigos](02_solucion/pseudocodigo/)
- [Diagramas](02_solucion/recursos/diagramas/)
- [DOCX editable](03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.docx)
- [PDF público](03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.pdf)
- [ZIP público](03_entrega/GA3-220501093-AA2-EV03_Taller_Funciones_Procedimientos.zip)

## Regeneración pública

Desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py preparar
python3 automatizacion/resolver_evidencias.py resolver --taller 5
```

La generación privada requiere proporcionar explícitamente un perfil y un destino externos;
no se ejecuta desde la automatización pública ni desde GitHub Actions.
