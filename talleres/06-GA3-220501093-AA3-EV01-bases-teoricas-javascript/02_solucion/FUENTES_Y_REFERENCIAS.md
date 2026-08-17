# Fuentes y decisiones — GA3-220501093-AA3-EV01

## Alcance verificado

El instrumento local y la guía de aprendizaje exigen un documento PDF de extensión libre
que desarrolle cuatro temas: diferencias entre lenguajes compilados e interpretados,
características de JavaScript, tipos de datos primitivos y operadores. Cada argumentación
debe apoyarse con imágenes ilustrativas y fuentes referenciadas.

- [Instrumento original](../01_enunciado/IE-GA3-220501093-AA3-EV01.pdf)
- [Guía de aprendizaje SENA, páginas 8–9](https://archivos.territorio.la/archivos/clases/Guianaprendizajen3___58631be32843215___.pdf)

## Fuentes técnicas primarias y de referencia

- [ECMA-262 — especificación vigente de ECMAScript](https://tc39.es/ecma262/)
- [MDN — panorama del lenguaje JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Language_overview)
- [MDN — tipos y estructuras de datos](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
- [MDN — expresiones y operadores](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
- [MDN — concepto de compilación](https://developer.mozilla.org/en-US/docs/Glossary/Compile)
- [V8 — canal de ejecución con Ignition y TurboFan](https://v8.dev/blog/launching-ignition-and-turbofan)

## Decisiones de contenido

- Se explican compilación e interpretación como estrategias de ejecución, no como cajas
  absolutas. Los motores modernos de JavaScript combinan interpretación y compilación JIT.
- Se documentan los siete primitivos vigentes: String, Number, BigInt, Boolean, Undefined,
  Symbol y Null. Object se presenta aparte porque no es primitivo.
- Los operadores se agrupan por propósito y se incluyen precedencia, cortocircuito,
  coerción, igualdad estricta y fusión nula.
- Las cuatro figuras son originales y se generan con Pillow. Cada pie identifica las fuentes
  conceptuales utilizadas; no se reutilizan imágenes de terceros.
- No se inventan ejercicios de vectores o matrices: pertenecen a una evidencia posterior.

## Modelo de las dos versiones

La solución académica es idéntica. `03_entrega` conserva únicamente la edición pública con
portada y metadatos genéricos. Si existe el perfil ignorado por Git, el generador crea un
solo PDF identificado en `04_entrega_personalizada.local`; el DOCX personalizado se usa
temporalmente y no se conserva. La automatización impide que esa ruta entre al índice.
