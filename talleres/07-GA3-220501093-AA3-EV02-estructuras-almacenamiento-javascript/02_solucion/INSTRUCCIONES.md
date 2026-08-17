# Instrucciones de ejecución — GA3-220501093-AA3-EV02

Las cuatro soluciones funcionan con Node.js 20 o superior y no requieren paquetes de
terceros.

Desde `02_solucion` se pueden comprobar todas las fuentes con:

```bash
npm run check
npm test
```

Cada programa también se puede utilizar de forma interactiva:

```bash
node codigo/01_figuras_planas.js
node codigo/02_analisis_edades.js
node codigo/03_mezclar_vectores.js
node codigo/04_encuesta_musical.js
```

El cuarto programa guarda la encuesta en un archivo JSON local. Ese archivo es un dato de
ejecución y no forma parte de la entrega ni del repositorio.

## Contenido

- `01_figuras_planas.js`: perímetro y área de triángulo, rectángulo, cuadrado y círculo.
- `02_analisis_edades.js`: validación y estadísticas de diez edades.
- `03_mezclar_vectores.js`: validación y mezcla lineal de dos vectores ascendentes.
- `04_encuesta_musical.js`: registro persistente de hasta seis personas y sus canciones.
- `pruebas/soluciones.test.js`: comprobaciones automatizadas de los cuatro problemas.

Todos los ejemplos incluidos en el código y en las pruebas son sintéticos.
