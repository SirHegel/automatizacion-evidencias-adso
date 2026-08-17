"use strict";

const readline = require("node:readline/promises");
const { stdin: input, stdout: output } = require("node:process");

const CANTIDAD_EDADES = 10;
const EDAD_MINIMA = 1;
const EDAD_MAXIMA = 120;

function validarEdad(edad) {
  if (!Number.isInteger(edad) || edad < EDAD_MINIMA || edad > EDAD_MAXIMA) {
    throw new RangeError(
      `La edad debe ser un entero entre ${EDAD_MINIMA} y ${EDAD_MAXIMA}.`,
    );
  }
  return edad;
}

function validarEdades(edades) {
  if (!Array.isArray(edades) || edades.length !== CANTIDAD_EDADES) {
    throw new RangeError(`Se requieren exactamente ${CANTIDAD_EDADES} edades.`);
  }
  return edades.map(validarEdad);
}

function analizarEdades(edades) {
  const valores = validarEdades(edades);
  const menoresDe18 = valores.filter((edad) => edad < 18);
  const entre18Y59 = valores.filter((edad) => edad >= 18 && edad <= 59);
  const mayoresOIgualesA60 = valores.filter((edad) => edad >= 60);
  const suma = valores.reduce((acumulado, edad) => acumulado + edad, 0);

  return Object.freeze({
    edades: Object.freeze([...valores]),
    grupos: Object.freeze({
      menoresDe18: Object.freeze(menoresDe18),
      entre18Y59: Object.freeze(entre18Y59),
      mayoresOIgualesA60: Object.freeze(mayoresOIgualesA60),
    }),
    conteos: Object.freeze({
      menoresDe18: menoresDe18.length,
      entre18Y59: entre18Y59.length,
      mayoresOIgualesA60: mayoresOIgualesA60.length,
    }),
    minimo: Math.min(...valores),
    maximo: Math.max(...valores),
    promedio: suma / valores.length,
  });
}

async function leerEdad(interfaz, posicion) {
  while (true) {
    const respuesta = (await interfaz.question(`Edad ${posicion}: `)).trim();
    const edad = Number(respuesta);
    try {
      return validarEdad(edad);
    } catch (error) {
      console.log(`${error.message} Vuelva a intentarlo.`);
    }
  }
}

function mostrarGrupo(etiqueta, edades) {
  const contenido = edades.length > 0 ? edades.join(", ") : "ninguna";
  console.log(`${etiqueta}: ${edades.length} (${contenido})`);
}

async function main() {
  const interfaz = readline.createInterface({ input, output });
  try {
    console.log(`Análisis de ${CANTIDAD_EDADES} edades`);
    const edades = [];
    for (let posicion = 1; posicion <= CANTIDAD_EDADES; posicion += 1) {
      edades.push(await leerEdad(interfaz, posicion));
    }

    const resultado = analizarEdades(edades);
    console.log("\nDistribución por grupos");
    mostrarGrupo("Menores de 18", resultado.grupos.menoresDe18);
    mostrarGrupo("Entre 18 y 59", resultado.grupos.entre18Y59);
    mostrarGrupo("Mayores o iguales a 60", resultado.grupos.mayoresOIgualesA60);
    console.log(`Edad mínima: ${resultado.minimo}`);
    console.log(`Edad máxima: ${resultado.maximo}`);
    console.log(`Promedio: ${resultado.promedio.toFixed(2)}`);
  } finally {
    interfaz.close();
  }
}

module.exports = {
  CANTIDAD_EDADES,
  EDAD_MINIMA,
  EDAD_MAXIMA,
  validarEdad,
  validarEdades,
  analizarEdades,
};

if (require.main === module) {
  main().catch((error) => {
    console.error(`Error: ${error.message}`);
    process.exitCode = 1;
  });
}
