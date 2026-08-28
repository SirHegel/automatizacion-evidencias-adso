"use strict";

const assert = require("node:assert/strict");
const { spawnSync } = require("node:child_process");
const { mkdtemp, readFile, rm, stat, writeFile } = require("node:fs/promises");
const { tmpdir } = require("node:os");
const path = require("node:path");
const test = require("node:test");

const figuras = require("../codigo/01_figuras_planas.js");
const edades = require("../codigo/02_analisis_edades.js");
const vectores = require("../codigo/03_mezclar_vectores.js");
const encuesta = require("../codigo/04_encuesta_musical.js");

function casiIgual(actual, esperado, tolerancia = Number.EPSILON * 16) {
  assert.ok(
    Math.abs(actual - esperado) <= tolerancia,
    `Se esperaba ${esperado}, pero se obtuvo ${actual}.`,
  );
}

function crearCorreo(alias) {
  const arroba = String.fromCharCode(64);
  return `${alias}${arroba}ejemplo.test`;
}

function crearPersona(indice, cambios = {}) {
  return {
    nombreCompleto: `Persona Sintética ${indice}`,
    numeroIdentificacion: `ID-${indice}`,
    fechaNacimiento: "2000-01-15",
    correoElectronico: crearCorreo(`persona${indice}`),
    ciudadResidencia: "Ciudad Verde",
    ciudadOrigen: "Villa Clara",
    cancionesFavoritas: [
      {
        artista: `Artista ${indice}`,
        titulo: `Canción ${indice}`,
      },
    ],
    ...cambios,
  };
}

async function conDirectorioTemporal(t) {
  const directorio = await mkdtemp(path.join(tmpdir(), "encuesta-sintetica-"));
  t.after(async () => {
    await rm(directorio, { recursive: true, force: true });
  });
  return directorio;
}

test("P1 calcula perímetros y áreas de las cuatro figuras", () => {
  assert.deepEqual(
    figuras.calcularTriangulo({ ladoA: 3, ladoB: 4, ladoC: 5, altura: 3 }),
    { figura: "triangulo", perimetro: 12, area: 6 },
  );
  assert.deepEqual(figuras.calcularRectangulo({ base: 4, altura: 2.5 }), {
    figura: "rectangulo",
    perimetro: 13,
    area: 10,
  });
  assert.deepEqual(figuras.calcularCuadrado({ lado: 3 }), {
    figura: "cuadrado",
    perimetro: 12,
    area: 9,
  });

  const circulo = figuras.calcularCirculo({ radio: 2 });
  assert.equal(circulo.figura, "circulo");
  casiIgual(circulo.perimetro, 4 * Math.PI);
  casiIgual(circulo.area, 4 * Math.PI);
});

test("P1 despacha por nombre u opción y formatea el resultado", () => {
  assert.deepEqual(figuras.calcularFigura(" 2 ", { base: 5, altura: 2 }), {
    figura: "rectangulo",
    perimetro: 14,
    area: 10,
  });
  assert.deepEqual(figuras.calcularFigura("CUADRADO", { lado: 4 }), {
    figura: "cuadrado",
    perimetro: 16,
    area: 16,
  });
  assert.match(
    figuras.formatearResultado(figuras.calcularCuadrado({ lado: 2 })),
    /Perímetro: 8\.00[\s\S]*Área: 4\.00/,
  );
});

test("P1 rechaza medidas, triángulos y tipos de figura inválidos", () => {
  for (const valor of [0, -1, Number.NaN, Number.POSITIVE_INFINITY, "2"]) {
    assert.throws(() => figuras.exigirPositivo(valor, "La medida"), RangeError);
  }
  assert.throws(() => figuras.validarTriangulo(1, 2, 3), RangeError);
  assert.throws(
    () => figuras.calcularTriangulo({ ladoA: 3, ladoB: 4, ladoC: 5, altura: 0 }),
    RangeError,
  );
  assert.throws(() => figuras.calcularFigura("hexagono", {}), RangeError);
});

test("P2 clasifica diez edades y calcula mínimo, máximo y promedio", () => {
  const entrada = [1, 17, 18, 25, 59, 60, 61, 80, 30, 45];
  const copia = [...entrada];
  const resultado = edades.analizarEdades(entrada);

  assert.deepEqual(entrada, copia, "el análisis no debe modificar la entrada");
  assert.deepEqual(resultado.grupos.menoresDe18, [1, 17]);
  assert.deepEqual(resultado.grupos.entre18Y59, [18, 25, 59, 30, 45]);
  assert.deepEqual(resultado.grupos.mayoresOIgualesA60, [60, 61, 80]);
  assert.deepEqual(resultado.conteos, {
    menoresDe18: 2,
    entre18Y59: 5,
    mayoresOIgualesA60: 3,
  });
  assert.equal(resultado.minimo, 1);
  assert.equal(resultado.maximo, 80);
  casiIgual(resultado.promedio, 39.6);
  assert.ok(Object.isFrozen(resultado));
  assert.ok(Object.isFrozen(resultado.edades));
});

test("P2 acepta los límites y rechaza edades fuera del dominio", () => {
  assert.equal(edades.validarEdad(edades.EDAD_MINIMA), edades.EDAD_MINIMA);
  assert.equal(edades.validarEdad(edades.EDAD_MAXIMA), edades.EDAD_MAXIMA);

  for (const valor of [0, 121, 18.5, "18", Number.NaN]) {
    assert.throws(() => edades.validarEdad(valor), RangeError);
  }
  assert.throws(() => edades.validarEdades([18, 19]), RangeError);
  assert.throws(() => edades.validarEdades("18,19"), RangeError);
  assert.throws(
    () => edades.analizarEdades([1, 2, 3, 4, 5, 6, 7, 8, 9, 121]),
    RangeError,
  );
});

test("P3 mezcla en orden ascendente y conserva los duplicados", () => {
  const vectorA = [-3, 1, 1, 8];
  const vectorB = [-2, 1, 4, 8, 9];
  const copiaA = [...vectorA];
  const copiaB = [...vectorB];

  assert.deepEqual(vectores.mezclarVectoresAscendentes(vectorA, vectorB), [
    -3,
    -2,
    1,
    1,
    1,
    4,
    8,
    8,
    9,
  ]);
  assert.deepEqual(vectorA, copiaA);
  assert.deepEqual(vectorB, copiaB);
  assert.deepEqual(vectores.mezclarVectoresAscendentes([2], [2]), [2, 2]);
});

test("P3 valida longitud, tipo, enteros y orden de cada vector", () => {
  assert.equal(vectores.validarLongitud(1), 1);
  assert.equal(vectores.validarLongitud(5), 5);
  for (const longitud of [0, 6, 2.5, "3"]) {
    assert.throws(() => vectores.validarLongitud(longitud), RangeError);
  }

  const original = [0, 2, 2, 7];
  const validado = vectores.validarVectorAscendente(original);
  assert.deepEqual(validado, original);
  assert.notStrictEqual(validado, original);
  assert.throws(() => vectores.validarVectorAscendente("1,2"), TypeError);
  assert.throws(() => vectores.validarVectorAscendente([]), RangeError);
  assert.throws(() => vectores.validarVectorAscendente([1, 2, 3, 4, 5, 6]), RangeError);
  assert.throws(() => vectores.validarVectorAscendente([1, 2.5, 3]), TypeError);
  assert.throws(() => vectores.validarVectorAscendente([1, 3, 2]), RangeError);
});

test("P4 normaliza una persona válida sin conservar espacios accidentales", () => {
  const persona = encuesta.normalizarPersona(
    crearPersona(1, {
      nombreCompleto: "  Persona Sintética 1  ",
      ciudadResidencia: "  Ciudad Verde ",
      cancionesFavoritas: [{ artista: " Artista Uno ", titulo: " Tema Uno " }],
    }),
  );

  assert.equal(persona.nombreCompleto, "Persona Sintética 1");
  assert.equal(persona.ciudadResidencia, "Ciudad Verde");
  assert.deepEqual(persona.cancionesFavoritas, [
    { artista: "Artista Uno", titulo: "Tema Uno" },
  ]);
  assert.ok(Object.isFrozen(persona));
  assert.ok(Object.isFrozen(persona.cancionesFavoritas));
});

test("P4 ejecuta altas, consulta, listado, modificación y eliminación sin mutar", () => {
  const primera = crearPersona(1);
  const segunda = crearPersona(2);
  const tercera = crearPersona(3);
  const vacia = [];

  const conPrimera = encuesta.agregarPersona(vacia, primera);
  const conDos = encuesta.agregarPersona(conPrimera, segunda);
  assert.deepEqual(vacia, []);
  assert.equal(conPrimera.length, 1);
  assert.equal(encuesta.obtenerPersonaPorPosicion(conDos, 2).numeroIdentificacion, "ID-2");
  assert.deepEqual(encuesta.listarPersonas(conDos), [
    {
      posicion: 1,
      nombreCompleto: "Persona Sintética 1",
      numeroIdentificacion: "ID-1",
      cantidadCanciones: 1,
    },
    {
      posicion: 2,
      nombreCompleto: "Persona Sintética 2",
      numeroIdentificacion: "ID-2",
      cantidadCanciones: 1,
    },
  ]);

  const modificadas = encuesta.modificarPersona(conDos, 1, tercera);
  assert.equal(modificadas[0].numeroIdentificacion, "ID-3");
  assert.equal(conDos[0].numeroIdentificacion, "ID-1");

  const restantes = encuesta.eliminarPersona(modificadas, 2);
  assert.deepEqual(restantes.map((persona) => persona.numeroIdentificacion), ["ID-3"]);
  assert.equal(modificadas.length, 2);
});

test("P4 impone el máximo de seis personas e identificaciones únicas", () => {
  let personas = [];
  for (let indice = 1; indice <= encuesta.MAX_PERSONAS; indice += 1) {
    personas = encuesta.agregarPersona(personas, crearPersona(indice));
  }
  assert.equal(personas.length, 6);
  assert.throws(() => encuesta.agregarPersona(personas, crearPersona(7)), RangeError);
  assert.throws(
    () => encuesta.validarEncuesta([crearPersona(1), crearPersona(2, { numeroIdentificacion: "id-1" })]),
    RangeError,
  );
  assert.throws(
    () => encuesta.modificarPersona(personas, 2, crearPersona(9, { numeroIdentificacion: "ID-1" })),
    RangeError,
  );
});

test("P4 rechaza posiciones y campos inválidos", () => {
  const personas = [crearPersona(1)];
  for (const posicion of [0, 2, 1.5, "1"]) {
    assert.throws(
      () => encuesta.obtenerPersonaPorPosicion(personas, posicion),
      RangeError,
    );
  }

  assert.throws(() => encuesta.normalizarPersona(null), TypeError);
  assert.throws(
    () => encuesta.normalizarPersona(crearPersona(1, { nombreCompleto: " " })),
    RangeError,
  );
  assert.throws(
    () => encuesta.normalizarPersona(crearPersona(1, { numeroIdentificacion: "ID con espacio" })),
    RangeError,
  );
  assert.throws(
    () => encuesta.normalizarPersona(crearPersona(1, { fechaNacimiento: "2001-02-29" })),
    RangeError,
  );
  assert.throws(
    () => encuesta.normalizarPersona(crearPersona(1, { fechaNacimiento: "2999-01-01" })),
    RangeError,
  );
  assert.throws(
    () => encuesta.normalizarPersona(crearPersona(1, { correoElectronico: "correo-invalido" })),
    RangeError,
  );
  assert.throws(
    () => encuesta.normalizarPersona(crearPersona(1, { cancionesFavoritas: [] })),
    RangeError,
  );
  assert.throws(
    () =>
      encuesta.normalizarPersona(
        crearPersona(1, {
          cancionesFavoritas: [
            { artista: "A", titulo: "Uno" },
            { artista: "B", titulo: "Dos" },
            { artista: "C", titulo: "Tres" },
            { artista: "D", titulo: "Cuatro" },
          ],
        }),
      ),
    RangeError,
  );
  assert.throws(
    () =>
      encuesta.normalizarPersona(
        crearPersona(1, { cancionesFavoritas: [{ artista: "", titulo: "Tema" }] }),
      ),
    RangeError,
  );
});

test("P4 guarda, recarga y reemplaza una encuesta en un archivo temporal", async (t) => {
  const directorio = await conDirectorioTemporal(t);
  const archivo = path.join(directorio, "encuesta.json");

  assert.deepEqual(await encuesta.cargarEncuesta(archivo), []);

  const inicial = [crearPersona(1), crearPersona(2)];
  await encuesta.guardarEncuesta(inicial, archivo);
  const contenido = await readFile(archivo, "utf8");
  assert.ok(contenido.endsWith("\n"));
  assert.equal((await stat(archivo)).mode & 0o777, 0o600);
  assert.deepEqual(await encuesta.cargarEncuesta(archivo), encuesta.validarEncuesta(inicial));

  const actualizada = encuesta.modificarPersona(inicial, 2, crearPersona(3));
  await encuesta.guardarEncuesta(actualizada, archivo);
  const recargada = await encuesta.cargarEncuesta(archivo);
  assert.deepEqual(
    recargada.map((persona) => persona.numeroIdentificacion),
    ["ID-1", "ID-3"],
  );
  await assert.rejects(readFile(`${archivo}.tmp`, "utf8"), { code: "ENOENT" });
});

test("P4 rechaza JSON dañado y datos inválidos antes de persistir", async (t) => {
  const directorio = await conDirectorioTemporal(t);
  const archivoDanado = path.join(directorio, "danado.json");
  const archivoEncuesta = path.join(directorio, "encuesta.json");

  await writeFile(archivoDanado, "{contenido incompleto", "utf8");
  await assert.rejects(encuesta.cargarEncuesta(archivoDanado), /información válida/);
  await assert.rejects(
    encuesta.guardarEncuesta([crearPersona(1, { fechaNacimiento: "fecha-invalida" })], archivoEncuesta),
    RangeError,
  );
  await assert.rejects(readFile(archivoEncuesta, "utf8"), { code: "ENOENT" });
});

test("P4 no permite redirigir la persistencia mediante el entorno", async (t) => {
  const directorio = await conDirectorioTemporal(t);
  const archivoExterno = path.join(directorio, "no-debe-leerse.json");
  const contenidoCentinela = "{contenido deliberadamente inválido";
  await writeFile(archivoExterno, contenidoCentinela, "utf8");

  const programa = path.join(__dirname, "../codigo/04_encuesta_musical.js");
  const ejecucion = spawnSync(process.execPath, [programa], {
    input: "0\n",
    encoding: "utf8",
    timeout: 5_000,
    env: { ...process.env, ENCUESTA_ARCHIVO: archivoExterno },
  });

  assert.equal(ejecucion.status, 0, ejecucion.stderr);
  assert.equal(await readFile(archivoExterno, "utf8"), contenidoCentinela);
  assert.doesNotMatch(ejecucion.stderr, /información válida/);
});
