"use strict";

const readline = require("node:readline/promises");
const { stdin: input, stdout: output } = require("node:process");

const LONGITUD_MINIMA = 1;
const LONGITUD_MAXIMA = 5;

function validarLongitud(longitud) {
  if (
    !Number.isInteger(longitud) ||
    longitud < LONGITUD_MINIMA ||
    longitud > LONGITUD_MAXIMA
  ) {
    throw new RangeError(
      `La longitud debe ser un entero entre ${LONGITUD_MINIMA} y ${LONGITUD_MAXIMA}.`,
    );
  }
  return longitud;
}

function validarVectorAscendente(vector, nombre = "El vector") {
  if (!Array.isArray(vector)) {
    throw new TypeError(`${nombre} debe ser un arreglo.`);
  }
  validarLongitud(vector.length);

  for (let indice = 0; indice < vector.length; indice += 1) {
    if (!Number.isInteger(vector[indice])) {
      throw new TypeError(`${nombre} solo puede contener números enteros.`);
    }
    if (indice > 0 && vector[indice] < vector[indice - 1]) {
      throw new RangeError(`${nombre} debe estar ordenado ascendentemente.`);
    }
  }
  return [...vector];
}

function mezclarVectoresAscendentes(vectorA, vectorB) {
  const primero = validarVectorAscendente(vectorA, "El vector A");
  const segundo = validarVectorAscendente(vectorB, "El vector B");
  const mezcla = [];
  let indiceA = 0;
  let indiceB = 0;

  while (indiceA < primero.length && indiceB < segundo.length) {
    if (primero[indiceA] <= segundo[indiceB]) {
      mezcla.push(primero[indiceA]);
      indiceA += 1;
    } else {
      mezcla.push(segundo[indiceB]);
      indiceB += 1;
    }
  }

  while (indiceA < primero.length) {
    mezcla.push(primero[indiceA]);
    indiceA += 1;
  }
  while (indiceB < segundo.length) {
    mezcla.push(segundo[indiceB]);
    indiceB += 1;
  }
  return mezcla;
}

async function leerEntero(interfaz, mensaje) {
  while (true) {
    const respuesta = (await interfaz.question(mensaje)).trim();
    const valor = Number(respuesta);
    if (Number.isInteger(valor)) {
      return valor;
    }
    console.log("Entrada inválida. Escriba un número entero.");
  }
}

async function leerLongitud(interfaz, nombre) {
  while (true) {
    const longitud = await leerEntero(
      interfaz,
      `Cantidad de elementos del vector ${nombre} (${LONGITUD_MINIMA}-${LONGITUD_MAXIMA}): `,
    );
    try {
      return validarLongitud(longitud);
    } catch (error) {
      console.log(error.message);
    }
  }
}

async function leerVectorAscendente(interfaz, nombre) {
  const longitud = await leerLongitud(interfaz, nombre);
  const vector = [];
  console.log(`Ingrese el vector ${nombre} en orden ascendente; se permiten duplicados.`);

  for (let posicion = 0; posicion < longitud; posicion += 1) {
    while (true) {
      const minimo = posicion === 0 ? "sin límite inferior" : `mínimo ${vector[posicion - 1]}`;
      const valor = await leerEntero(
        interfaz,
        `Elemento ${posicion + 1} (${minimo}): `,
      );
      if (posicion === 0 || valor >= vector[posicion - 1]) {
        vector.push(valor);
        break;
      }
      console.log("El valor rompe el orden ascendente. Ingréselo nuevamente.");
    }
  }
  return vector;
}

async function main() {
  const interfaz = readline.createInterface({ input, output });
  try {
    console.log("Mezcla lineal de dos vectores ascendentes");
    const vectorA = await leerVectorAscendente(interfaz, "A");
    const vectorB = await leerVectorAscendente(interfaz, "B");
    const mezcla = mezclarVectoresAscendentes(vectorA, vectorB);
    console.log(`\nVector A: [${vectorA.join(", ")}]`);
    console.log(`Vector B: [${vectorB.join(", ")}]`);
    console.log(`Mezcla:   [${mezcla.join(", ")}]`);
  } finally {
    interfaz.close();
  }
}

module.exports = {
  LONGITUD_MINIMA,
  LONGITUD_MAXIMA,
  validarLongitud,
  validarVectorAscendente,
  mezclarVectoresAscendentes,
};

if (require.main === module) {
  main().catch((error) => {
    console.error(`Error: ${error.message}`);
    process.exitCode = 1;
  });
}
