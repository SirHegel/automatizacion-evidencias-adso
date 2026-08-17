// GA3-220501093-AA2-EV03
// Problema 10: mostrar la tabla de multiplicar en orden decreciente.

SubProceso valido <- NumeroDeTablaValido(numero)
    Definir valido Como Logico;
    valido <- numero >= 1 Y numero <= 10 Y numero = Trunc(numero);
FinSubProceso

SubProceso MostrarTablaDecreciente(numero)
    Definir multiplicador Como Entero;

    Para multiplicador <- 10 Hasta 1 Con Paso -1 Hacer
        Escribir numero, " x ", multiplicador, " = ", numero * multiplicador;
    FinPara
FinSubProceso

Proceso TablaMultiplicarDecreciente
    Definir numeroIngresado Como Real;
    Definir numero Como Entero;

    Repetir
        Escribir "Ingrese un numero entero entre 1 y 10:";
        Leer numeroIngresado;
        Si NO NumeroDeTablaValido(numeroIngresado) Entonces
            Escribir "Dato invalido. Debe ser un entero entre 1 y 10.";
        FinSi
    Hasta Que NumeroDeTablaValido(numeroIngresado)

    numero <- Trunc(numeroIngresado);
    MostrarTablaDecreciente(numero);
FinProceso
