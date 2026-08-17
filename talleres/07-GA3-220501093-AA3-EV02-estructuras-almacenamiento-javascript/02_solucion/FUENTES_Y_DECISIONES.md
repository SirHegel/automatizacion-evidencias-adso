# Fuentes y decisiones — GA3-220501093-AA3-EV02

## Alcance verificado

El instrumento local contiene cuatro indicadores binarios: una solución coherente en
JavaScript para cada problema. La guía de aprendizaje precisa los enunciados y exige un
único archivo ZIP con todas las soluciones.

- [Instrumento original](../01_enunciado/IE-GA3-220501093-AA3-EV02.pdf)
- [Guía de aprendizaje SENA, páginas físicas 9–10](https://archivos.territorio.la/archivos/clases/Guianaprendizajen3___58631be32843215___.pdf)
- [MDN — arreglos en JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Node.js — sistema de archivos](https://nodejs.org/api/fs.html)
- [Node.js — interfaz de lectura](https://nodejs.org/api/readline.html)
- [Node.js — ejecutor de pruebas](https://nodejs.org/api/test.html)

## Decisiones de solución

- El problema 1 usa `2 × π × r` para el perímetro del círculo. La tabla de la guía imprime
  `2 × π × r²`, que corresponde a un error tipográfico; el área sí es `π × r²`.
- En el problema 2 se usan categorías excluyentes: menor de edad, de 1 a 17 años;
  adulto, de 18 a 59; adulto mayor, desde los 60 años.
- El problema 3 acepta de uno a cinco elementos por vector. Esta lectura respeta el límite
  indicado y el ejemplo oficial, cuyos vectores tienen longitudes diferentes.
- La mezcla se implementa con dos índices, en tiempo lineal, y conserva los duplicados.
- El problema 4 implementa las dos opciones mínimas de la guía y agrega modificación,
  eliminación, listado y persistencia JSON para atender los criterios generales del
  instrumento sobre administración de información.
- Los datos de prueba son sintéticos. El archivo JSON que se crea al ejecutar el menú no se
  incluye en los ZIP generados.

## Modelo de publicación

`03_entrega` contiene exclusivamente el ZIP público genérico que se publica en GitHub.
`04_entrega_personalizada.local` contiene un único ZIP personalizado, listo para seleccionar
y cargar en la plataforma SENA. La segunda carpeta está ignorada por Git.
