// GA3-220501093-AA2-EV03
// Problema 9: calcular el producto de los enteros desde 1 hasta N.
// Se admite N = 0 y se aplica la convencion de producto vacio: 0! = 1.

SubProceso valido <- EsEnteroNoNegativo(numero)
    Definir valido Como Logico;
    valido <- numero >= 0 Y numero = Trunc(numero);
FinSubProceso

SubProceso producto <- CalcularProductoUnoHastaN(n)
    Definir producto Como Real;
    Definir factor Como Entero;

    producto <- 1;
    Para factor <- 1 Hasta n Con Paso 1 Hacer
        producto <- producto * factor;
    FinPara
FinSubProceso

Proceso ProductoUnoHastaN
    Definir numeroIngresado, producto Como Real;
    Definir n Como Entero;

    Repetir
        Escribir "Ingrese un numero entero no negativo:";
        Leer numeroIngresado;
        Si NO EsEnteroNoNegativo(numeroIngresado) Entonces
            Escribir "Dato invalido. Debe ser un entero mayor o igual a cero.";
        FinSi
    Hasta Que EsEnteroNoNegativo(numeroIngresado)

    n <- Trunc(numeroIngresado);
    producto <- CalcularProductoUnoHastaN(n);
    Escribir "El producto desde 1 hasta ", n, " es ", producto, ".";
FinProceso
