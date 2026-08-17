# Informe público de resolución — GA3-220501093-AA3-EV01

## Estado

- **Producto:** bases teóricas de estructuras de almacenamiento en memoria.
- **Entrega pública:** DOCX editable y PDF, sin información personal del aprendiz.
- **Entrega personalizada local:** un único PDF listo para subir, dentro de
  `04_entrega_personalizada.local`, excluido de Git.
- **Cobertura:** cinco de cinco indicadores del instrumento.

## Interpretación del trabajo

La [guía de aprendizaje SENA](https://archivos.territorio.la/archivos/clases/Guianaprendizajen3___58631be32843215___.pdf),
en sus páginas físicas 8 y 9, pide un documento PDF de extensión libre. Aunque la actividad
general menciona arreglos, esta evidencia de conocimiento evalúa exactamente cuatro temas:

1. diferencias entre lenguajes compilados e interpretados;
2. características principales de JavaScript;
3. tipos de datos primitivos y sus usos;
4. operadores en JavaScript.

El quinto indicador exige imágenes ilustrativas y referencias. Por eso se elaboraron cuatro
figuras originales, una por núcleo temático, con su fuente conceptual en cada pie.

## Contenido construido

El documento se organizó en doce páginas: portada; propósito y ruta; dos páginas sobre
estrategias de ejecución; dos sobre JavaScript; dos sobre primitivos; dos sobre operadores;
matriz de cumplimiento y referencias.

Se corrigió una simplificación frecuente: JavaScript no debe describirse hoy como
exclusivamente interpretado. La especificación define el lenguaje y cada motor decide su
estrategia; V8, por ejemplo, combina el intérprete Ignition y el compilador optimizador
TurboFan. También se incorporaron los siete primitivos actuales y ejemplos que distinguen
igualdad estricta, coerción, precedencia, cortocircuito y fusión nula.

## Trazabilidad

| Indicador | Evidencia dentro del documento |
|---:|---|
| 1 | Capítulo 1 y figura 1: comparación y ejecución híbrida moderna. |
| 2 | Capítulo 2 y figura 2: estándar, paradigmas, prototipos y entornos. |
| 3 | Capítulo 3 y figura 3: siete primitivos, usos, ejemplos y advertencias. |
| 4 | Capítulo 4 y figura 4: familias, precedencia y ejemplos verificables. |
| 5 | Cuatro ilustraciones propias, citas numeradas y bibliografía final. |

## Privacidad y publicación

Los archivos públicos no contienen número de documento, contacto, grupo, instructor,
centro, ciudad ni firma. El perfil y el PDF personalizado permanecen ignorados por Git.
`03_entrega` contiene exclusivamente productos públicos; la única entrega con los datos del
aprendiz se genera como `04_entrega_personalizada.local/ENTREGAR_GA3-220501093-AA3-EV01.pdf`.
La auditoría se detiene si detecta que una ruta local fue agregada al índice.

## Archivos públicos

- [Instrumento](01_enunciado/IE-GA3-220501093-AA3-EV01.pdf)
- [Fuentes y decisiones](02_solucion/FUENTES_Y_REFERENCIAS.md)
- [Generador](02_solucion/generar_entrega.py)
- [DOCX](03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.docx)
- [PDF](03_entrega/GA3-220501093-AA3-EV01_Bases_Teoricas_JavaScript.pdf)

## Regeneración

Desde la raíz del repositorio:

```bash
python3 automatizacion/resolver_evidencias.py preparar
python3 automatizacion/resolver_evidencias.py resolver --taller 6
```

Cuando existe `perfil-aprendiz.local.json`, el mismo generador crea automáticamente el único
PDF personalizado listo para entregar. El DOCX que incorpora esos datos existe solo de
forma temporal durante la exportación y no se conserva. Ningún dato personal está
codificado en el generador.

Un clon de GitHub no incluye el perfil, el directorio personalizado ni su PDF. Para
reconstruirlo en otro equipo se debe copiar el perfil por un medio privado y ejecutar el
generador. La entrega local tampoco es una copia de seguridad y puede eliminarse con
operaciones como `git clean -fdx`.
