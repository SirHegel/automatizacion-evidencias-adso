"use strict";

const fs = require("node:fs/promises");
const path = require("node:path");
const readline = require("node:readline/promises");
const { stdin: input, stdout: output } = require("node:process");

const MAX_PERSONAS = 6;
const MIN_CANCIONES = 1;
const MAX_CANCIONES = 3;
const ARCHIVO_PREDETERMINADO = path.join(__dirname, "encuesta_musical.local.json");

function exigirTexto(valor, campo, maximo = 100) {
  if (typeof valor !== "string") {
    throw new TypeError(`${campo} debe ser texto.`);
  }
  const limpio = valor.trim();
  if (limpio.length === 0 || limpio.length > maximo) {
    throw new RangeError(`${campo} debe contener entre 1 y ${maximo} caracteres.`);
  }
  return limpio;
}

function validarNumeroIdentificacion(valor) {
  const limpio = exigirTexto(valor, "El número de identificación", 30);
  if (!/^[A-Za-z0-9-]+$/.test(limpio)) {
    throw new RangeError(
      "El número de identificación solo admite letras, números y guiones.",
    );
  }
  return limpio;
}

function validarFecha(fecha) {
  const limpia = exigirTexto(fecha, "La fecha de nacimiento", 10);
  const coincidencia = /^(\d{4})-(\d{2})-(\d{2})$/.exec(limpia);
  if (!coincidencia) {
    throw new RangeError("La fecha de nacimiento debe usar el formato AAAA-MM-DD.");
  }
  const [, anioTexto, mesTexto, diaTexto] = coincidencia;
  const anio = Number(anioTexto);
  const mes = Number(mesTexto);
  const dia = Number(diaTexto);
  const fechaUtc = new Date(Date.UTC(anio, mes - 1, dia));
  const esMismaFecha =
    fechaUtc.getUTCFullYear() === anio &&
    fechaUtc.getUTCMonth() === mes - 1 &&
    fechaUtc.getUTCDate() === dia;
  if (!esMismaFecha) {
    throw new RangeError("La fecha de nacimiento no existe en el calendario.");
  }
  if (fechaUtc > new Date()) {
    throw new RangeError("La fecha de nacimiento no puede estar en el futuro.");
  }
  return limpia;
}

function validarCorreo(correoElectronico) {
  const limpio = exigirTexto(correoElectronico, "El correo electrónico", 120);
  const patron = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!patron.test(limpio)) {
    throw new RangeError("El correo electrónico no tiene un formato válido.");
  }
  return limpio;
}

function normalizarCancion(cancion) {
  if (!cancion || typeof cancion !== "object" || Array.isArray(cancion)) {
    throw new TypeError("Cada canción debe contener artista y título.");
  }
  return Object.freeze({
    artista: exigirTexto(cancion.artista, "El artista", 100),
    titulo: exigirTexto(cancion.titulo, "El título", 120),
  });
}

function validarCanciones(cancionesFavoritas) {
  if (
    !Array.isArray(cancionesFavoritas) ||
    cancionesFavoritas.length < MIN_CANCIONES ||
    cancionesFavoritas.length > MAX_CANCIONES
  ) {
    throw new RangeError(
      `Se requieren entre ${MIN_CANCIONES} y ${MAX_CANCIONES} canciones favoritas.`,
    );
  }
  return Object.freeze(cancionesFavoritas.map(normalizarCancion));
}

function normalizarPersona(persona) {
  if (!persona || typeof persona !== "object" || Array.isArray(persona)) {
    throw new TypeError("La persona debe representarse mediante un objeto.");
  }
  return Object.freeze({
    nombreCompleto: exigirTexto(persona.nombreCompleto, "El nombre completo", 100),
    numeroIdentificacion: validarNumeroIdentificacion(persona.numeroIdentificacion),
    fechaNacimiento: validarFecha(persona.fechaNacimiento),
    correoElectronico: validarCorreo(persona.correoElectronico),
    ciudadResidencia: exigirTexto(persona.ciudadResidencia, "La ciudad de residencia", 80),
    ciudadOrigen: exigirTexto(persona.ciudadOrigen, "La ciudad de origen", 80),
    cancionesFavoritas: validarCanciones(persona.cancionesFavoritas),
  });
}

function validarEncuesta(personas) {
  if (!Array.isArray(personas)) {
    throw new TypeError("La encuesta debe ser un arreglo de personas.");
  }
  if (personas.length > MAX_PERSONAS) {
    throw new RangeError(`La encuesta admite como máximo ${MAX_PERSONAS} personas.`);
  }
  const normalizadas = personas.map(normalizarPersona);
  const identificaciones = new Set();
  for (const persona of normalizadas) {
    const clave = persona.numeroIdentificacion.toLowerCase();
    if (identificaciones.has(clave)) {
      throw new RangeError("Cada número de identificación debe ser único.");
    }
    identificaciones.add(clave);
  }
  return normalizadas;
}

function agregarPersona(personas, nuevaPersona) {
  const actuales = validarEncuesta(personas);
  if (actuales.length >= MAX_PERSONAS) {
    throw new RangeError(`No se pueden registrar más de ${MAX_PERSONAS} personas.`);
  }
  return validarEncuesta([...actuales, normalizarPersona(nuevaPersona)]);
}

function indiceDesdePosicion(personas, posicion) {
  if (!Number.isInteger(posicion) || posicion < 1 || posicion > personas.length) {
    throw new RangeError(`La posición debe estar entre 1 y ${personas.length}.`);
  }
  return posicion - 1;
}

function obtenerPersonaPorPosicion(personas, posicion) {
  const actuales = validarEncuesta(personas);
  const indice = indiceDesdePosicion(actuales, posicion);
  return actuales[indice];
}

function modificarPersona(personas, posicion, personaActualizada) {
  const actuales = validarEncuesta(personas);
  const indice = indiceDesdePosicion(actuales, posicion);
  const copia = [...actuales];
  copia[indice] = normalizarPersona(personaActualizada);
  return validarEncuesta(copia);
}

function eliminarPersona(personas, posicion) {
  const actuales = validarEncuesta(personas);
  const indice = indiceDesdePosicion(actuales, posicion);
  return actuales.filter((_, indiceActual) => indiceActual !== indice);
}

function listarPersonas(personas) {
  return validarEncuesta(personas).map((persona, indice) =>
    Object.freeze({
      posicion: indice + 1,
      nombreCompleto: persona.nombreCompleto,
      numeroIdentificacion: persona.numeroIdentificacion,
      cantidadCanciones: persona.cancionesFavoritas.length,
    }),
  );
}

async function cargarEncuesta(rutaArchivo = ARCHIVO_PREDETERMINADO) {
  try {
    const contenido = await fs.readFile(rutaArchivo, "utf8");
    return validarEncuesta(JSON.parse(contenido));
  } catch (error) {
    if (error.code === "ENOENT") {
      return [];
    }
    if (error instanceof SyntaxError) {
      throw new Error("El archivo JSON no contiene información válida.");
    }
    throw error;
  }
}

async function guardarEncuesta(personas, rutaArchivo = ARCHIVO_PREDETERMINADO) {
  const normalizadas = validarEncuesta(personas);
  const temporal = `${rutaArchivo}.tmp`;
  const contenido = `${JSON.stringify(normalizadas, null, 2)}\n`;
  try {
    await fs.writeFile(temporal, contenido, { encoding: "utf8", mode: 0o600 });
    await fs.rename(temporal, rutaArchivo);
    await fs.chmod(rutaArchivo, 0o600);
  } finally {
    await fs.rm(temporal, { force: true });
  }
}

async function leerTexto(interfaz, mensaje, validador = null) {
  while (true) {
    const respuesta = await interfaz.question(mensaje);
    try {
      return validador ? validador(respuesta) : exigirTexto(respuesta, "El valor");
    } catch (error) {
      console.log(`${error.message} Vuelva a intentarlo.`);
    }
  }
}

async function leerEnteroEnRango(interfaz, mensaje, minimo, maximo) {
  while (true) {
    const respuesta = (await interfaz.question(mensaje)).trim();
    const valor = Number(respuesta);
    if (Number.isInteger(valor) && valor >= minimo && valor <= maximo) {
      return valor;
    }
    console.log(`Escriba un entero entre ${minimo} y ${maximo}.`);
  }
}

async function solicitarCanciones(interfaz) {
  const cantidad = await leerEnteroEnRango(
    interfaz,
    `Cantidad de canciones favoritas (${MIN_CANCIONES}-${MAX_CANCIONES}): `,
    MIN_CANCIONES,
    MAX_CANCIONES,
  );
  const canciones = [];
  for (let posicion = 1; posicion <= cantidad; posicion += 1) {
    console.log(`Canción ${posicion}`);
    canciones.push({
      artista: await leerTexto(interfaz, "  Artista: "),
      titulo: await leerTexto(interfaz, "  Título: "),
    });
  }
  return canciones;
}

async function solicitarPersona(interfaz) {
  return normalizarPersona({
    nombreCompleto: await leerTexto(interfaz, "Nombre completo: "),
    numeroIdentificacion: await leerTexto(
      interfaz,
      "Número de identificación: ",
      validarNumeroIdentificacion,
    ),
    fechaNacimiento: await leerTexto(
      interfaz,
      "Fecha de nacimiento (AAAA-MM-DD): ",
      validarFecha,
    ),
    correoElectronico: await leerTexto(
      interfaz,
      "Correo electrónico: ",
      validarCorreo,
    ),
    ciudadResidencia: await leerTexto(interfaz, "Ciudad de residencia: "),
    ciudadOrigen: await leerTexto(interfaz, "Ciudad de origen: "),
    cancionesFavoritas: await solicitarCanciones(interfaz),
  });
}

function imprimirPersona(persona, posicion) {
  console.log(`\nPersona ${posicion}`);
  console.log(`Nombre: ${persona.nombreCompleto}`);
  console.log(`Número de identificación: ${persona.numeroIdentificacion}`);
  console.log(`Fecha de nacimiento: ${persona.fechaNacimiento}`);
  console.log(`Correo electrónico: ${persona.correoElectronico}`);
  console.log(`Ciudad de residencia: ${persona.ciudadResidencia}`);
  console.log(`Ciudad de origen: ${persona.ciudadOrigen}`);
  console.log("Canciones favoritas:");
  persona.cancionesFavoritas.forEach((cancion, indice) => {
    console.log(`  ${indice + 1}. ${cancion.titulo} — ${cancion.artista}`);
  });
}

function imprimirListado(personas) {
  const listado = listarPersonas(personas);
  if (listado.length === 0) {
    console.log("No hay personas registradas.");
    return;
  }
  console.log("\nPersonas registradas");
  for (const persona of listado) {
    console.log(
      `${persona.posicion}. ${persona.nombreCompleto} | identificación: ${persona.numeroIdentificacion} | canciones: ${persona.cantidadCanciones}`,
    );
  }
}

async function leerPosicion(interfaz, personas, accion) {
  if (personas.length === 0) {
    console.log("No hay personas registradas.");
    return null;
  }
  imprimirListado(personas);
  return leerEnteroEnRango(
    interfaz,
    `Posición que desea ${accion} (1-${personas.length}): `,
    1,
    personas.length,
  );
}

async function ejecutarMenu(interfaz, rutaArchivo) {
  let personas = await cargarEncuesta(rutaArchivo);
  let continuar = true;

  while (continuar) {
    console.log(
      "\nEncuesta musical\n" +
        "1. Agregar persona\n" +
        "2. Mostrar persona por posición\n" +
        "3. Modificar persona\n" +
        "4. Eliminar persona\n" +
        "5. Listar personas\n" +
        "0. Salir",
    );
    const opcion = await leerEnteroEnRango(interfaz, "Opción: ", 0, 5);

    if (opcion === 1) {
      try {
        personas = agregarPersona(personas, await solicitarPersona(interfaz));
        await guardarEncuesta(personas, rutaArchivo);
        console.log("Persona agregada y encuesta guardada.");
      } catch (error) {
        console.log(`No se pudo agregar: ${error.message}`);
      }
    } else if (opcion === 2) {
      const posicion = await leerPosicion(interfaz, personas, "mostrar");
      if (posicion !== null) {
        imprimirPersona(obtenerPersonaPorPosicion(personas, posicion), posicion);
      }
    } else if (opcion === 3) {
      const posicion = await leerPosicion(interfaz, personas, "modificar");
      if (posicion !== null) {
        try {
          personas = modificarPersona(
            personas,
            posicion,
            await solicitarPersona(interfaz),
          );
          await guardarEncuesta(personas, rutaArchivo);
          console.log("Persona modificada y encuesta guardada.");
        } catch (error) {
          console.log(`No se pudo modificar: ${error.message}`);
        }
      }
    } else if (opcion === 4) {
      const posicion = await leerPosicion(interfaz, personas, "eliminar");
      if (posicion !== null) {
        personas = eliminarPersona(personas, posicion);
        await guardarEncuesta(personas, rutaArchivo);
        console.log("Persona eliminada y encuesta guardada.");
      }
    } else if (opcion === 5) {
      imprimirListado(personas);
    } else {
      continuar = false;
    }
  }
}

async function main() {
  const interfaz = readline.createInterface({ input, output });
  const rutaArchivo = process.env.ENCUESTA_ARCHIVO || ARCHIVO_PREDETERMINADO;
  try {
    await ejecutarMenu(interfaz, rutaArchivo);
  } finally {
    interfaz.close();
  }
}

module.exports = {
  MAX_PERSONAS,
  MIN_CANCIONES,
  MAX_CANCIONES,
  ARCHIVO_PREDETERMINADO,
  exigirTexto,
  validarNumeroIdentificacion,
  validarFecha,
  validarCorreo,
  normalizarCancion,
  validarCanciones,
  normalizarPersona,
  validarEncuesta,
  agregarPersona,
  obtenerPersonaPorPosicion,
  modificarPersona,
  eliminarPersona,
  listarPersonas,
  cargarEncuesta,
  guardarEncuesta,
};

if (require.main === module) {
  main().catch((error) => {
    console.error(`Error: ${error.message}`);
    process.exitCode = 1;
  });
}
