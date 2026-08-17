# Informe público de resolución — GA3-220501093-AA3-EV02

## Estado

- **Producto:** resolución de cuatro problemas algorítmicos en JavaScript.
- **Entrega pública:** un ZIP genérico, reproducible y sin datos personales.
- **Entrega para SENA:** un único ZIP personalizado dentro de
  `04_entrega_personalizada.local`, excluido de Git.
- **Cobertura:** cuatro de cuatro indicadores del instrumento.

## Alcance

La [guía de aprendizaje SENA](https://archivos.territorio.la/archivos/clases/Guianaprendizajen3___58631be32843215___.pdf),
en las páginas físicas 9 y 10, exige resolver cuatro problemas con JavaScript y reunir las
soluciones en un solo ZIP con el nombre del estudiante.

No se solicita un sistema único que integre los cuatro casos. La evidencia está compuesta
por cuatro programas independientes; el cuarto sí funciona como una miniaplicación de
encuesta musical con menú, almacenamiento de personas y persistencia en un archivo JSON.

## Trazabilidad

| Indicador | Implementación | Comprobaciones |
|---:|---|---|
| 1 | `01_figuras_planas.js` | Fórmulas, dominios inválidos y desigualdad triangular. |
| 2 | `02_analisis_edades.js` | Diez edades, rangos, categorías, mínimo, máximo y promedio. |
| 3 | `03_mezclar_vectores.js` | Orden ascendente, límite de cinco, mezcla y duplicados. |
| 4 | `04_encuesta_musical.js` | Registro, consulta, modificación, eliminación y persistencia JSON. |

Las 13 pruebas se encuentran en `02_solucion/pruebas/soluciones.test.js` y se ejecutan
durante la generación del ZIP.

## Decisiones relevantes

La circunferencia se calcula con `2 × π × r`. La tabla de la guía imprime por error
`2 × π × r²`; aplicar esa expresión produciría un perímetro dimensionalmente incorrecto.

El cuarto programa cubre las opciones mínimas de agregar y consultar por posición. También
incorpora modificación, eliminación, listado y persistencia para satisfacer los criterios
generales del instrumento sobre administración de información.

## Separación de archivos

- `03_entrega` es una zona exclusivamente pública y contiene el ZIP de GitHub.
- `04_entrega_personalizada.local` aparece solo en el equipo local y contiene exactamente
  un archivo ZIP: ese es el que debe seleccionarse al entregar en la plataforma SENA.
- Las fuentes, pruebas y documentación quedan en `02_solucion`; no son archivos alternativos
  que el aprendiz deba escoger para la entrega.

La automatización bloquea cualquier intento de rastrear el perfil o una ruta `.local`.

## Regeneración

Desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py resolver --taller 7
```

En un clon sin perfil se genera únicamente el ZIP público. Cuando existe el perfil local,
se crea además el único ZIP personalizado listo para entregar.
