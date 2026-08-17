"use strict";

const readline = require("node:readline/promises");
const { stdin: input, stdout: output } = require("node:process");

const TIPOS_FIGURA = Object.freeze({
  TRIANGULO: "triangulo",
  RECTANGULO: "rectangulo",
  CUADRADO: "cuadrado",
  CIRCULO: "circulo",
});

function exigirPositivo(valor, nombre) {
  if (typeof valor !== "number" || !Number.isFinite(valor) || valor <= 0) {
    throw new RangeError(`${nombre} debe ser un número positivo.`);
  }
  return valor;
}

function validarTriangulo(ladoA, ladoB, ladoC) {
  exigirPositivo(ladoA, "El lado A");
  exigirPositivo(ladoB, "El lado B");
  exigirPositivo(ladoC, "El lado C");

  const esValido =
    ladoA + ladoB > ladoC &&
    ladoA + ladoC > ladoB &&
    ladoB + ladoC > ladoA;

  if (!esValido) {
    throw new RangeError(
      "Los lados no forman un triángulo: la suma de dos lados debe superar al tercero.",
    );
  }
  return true;
}

function calcularTriangulo({ ladoA, ladoB, ladoC, altura }) {
  validarTriangulo(ladoA, ladoB, ladoC);
  exigirPositivo(altura, "La altura");
  return Object.freeze({
    figura: TIPOS_FIGURA.TRIANGULO,
    perimetro: ladoA + ladoB + ladoC,
    area: (ladoB * altura) / 2,
  });
}

function calcularRectangulo({ base, altura }) {
  exigirPositivo(base, "La base");
  exigirPositivo(altura, "La altura");
  return Object.freeze({
    figura: TIPOS_FIGURA.RECTANGULO,
    perimetro: 2 * (base + altura),
    area: base * altura,
  });
}

function calcularCuadrado({ lado }) {
  exigirPositivo(lado, "El lado");
  return Object.freeze({
    figura: TIPOS_FIGURA.CUADRADO,
    perimetro: 4 * lado,
    area: lado ** 2,
  });
}

function calcularCirculo({ radio }) {
  exigirPositivo(radio, "El radio");
  return Object.freeze({
    figura: TIPOS_FIGURA.CIRCULO,
    perimetro: 2 * Math.PI * radio,
    area: Math.PI * radio ** 2,
  });
}

function normalizarTipoFigura(tipo) {
  const valor = String(tipo).trim().toLowerCase();
  const equivalencias = {
    "1": TIPOS_FIGURA.TRIANGULO,
    triangulo: TIPOS_FIGURA.TRIANGULO,
    "2": TIPOS_FIGURA.RECTANGULO,
    rectangulo: TIPOS_FIGURA.RECTANGULO,
    "3": TIPOS_FIGURA.CUADRADO,
    cuadrado: TIPOS_FIGURA.CUADRADO,
    "4": TIPOS_FIGURA.CIRCULO,
    circulo: TIPOS_FIGURA.CIRCULO,
  };
  const normalizado = equivalencias[valor];
  if (!normalizado) {
    throw new RangeError("La figura debe ser triángulo, rectángulo, cuadrado o círculo.");
  }
  return normalizado;
}

function calcularFigura(tipo, medidas) {
  const figura = normalizarTipoFigura(tipo);
  const calculadoras = {
    [TIPOS_FIGURA.TRIANGULO]: calcularTriangulo,
    [TIPOS_FIGURA.RECTANGULO]: calcularRectangulo,
    [TIPOS_FIGURA.CUADRADO]: calcularCuadrado,
    [TIPOS_FIGURA.CIRCULO]: calcularCirculo,
  };
  return calculadoras[figura](medidas);
}

async function leerNumeroPositivo(interfaz, mensaje) {
  while (true) {
    const respuesta = (await interfaz.question(mensaje)).trim().replace(",", ".");
    const valor = Number(respuesta);
    if (Number.isFinite(valor) && valor > 0) {
      return valor;
    }
    console.log("Entrada inválida. Escriba un número mayor que cero.");
  }
}

async function leerFigura(interfaz) {
  while (true) {
    console.log("\n1. Triángulo\n2. Rectángulo\n3. Cuadrado\n4. Círculo");
    const opcion = await interfaz.question("Seleccione una figura: ");
    try {
      return normalizarTipoFigura(opcion);
    } catch (error) {
      console.log(error.message);
    }
  }
}

async function solicitarMedidas(interfaz, figura) {
  if (figura === TIPOS_FIGURA.TRIANGULO) {
    while (true) {
      const ladoA = await leerNumeroPositivo(interfaz, "Lado A: ");
      const ladoB = await leerNumeroPositivo(interfaz, "Lado B (base): ");
      const ladoC = await leerNumeroPositivo(interfaz, "Lado C: ");
      const altura = await leerNumeroPositivo(interfaz, "Altura respecto al lado B: ");
      try {
        validarTriangulo(ladoA, ladoB, ladoC);
        return { ladoA, ladoB, ladoC, altura };
      } catch (error) {
        console.log(`${error.message} Ingrese nuevamente las medidas.`);
      }
    }
  }
  if (figura === TIPOS_FIGURA.RECTANGULO) {
    return {
      base: await leerNumeroPositivo(interfaz, "Base: "),
      altura: await leerNumeroPositivo(interfaz, "Altura: "),
    };
  }
  if (figura === TIPOS_FIGURA.CUADRADO) {
    return { lado: await leerNumeroPositivo(interfaz, "Lado: ") };
  }
  return { radio: await leerNumeroPositivo(interfaz, "Radio: ") };
}

function formatearResultado(resultado) {
  return [
    `Figura: ${resultado.figura}`,
    `Perímetro: ${resultado.perimetro.toFixed(2)}`,
    `Área: ${resultado.area.toFixed(2)}`,
  ].join("\n");
}

async function main() {
  const interfaz = readline.createInterface({ input, output });
  try {
    console.log("Cálculo de área y perímetro de figuras planas");
    const figura = await leerFigura(interfaz);
    const medidas = await solicitarMedidas(interfaz, figura);
    console.log(`\n${formatearResultado(calcularFigura(figura, medidas))}`);
  } finally {
    interfaz.close();
  }
}

module.exports = {
  TIPOS_FIGURA,
  exigirPositivo,
  validarTriangulo,
  calcularTriangulo,
  calcularRectangulo,
  calcularCuadrado,
  calcularCirculo,
  normalizarTipoFigura,
  calcularFigura,
  formatearResultado,
};

if (require.main === module) {
  main().catch((error) => {
    console.error(`Error: ${error.message}`);
    process.exitCode = 1;
  });
}
