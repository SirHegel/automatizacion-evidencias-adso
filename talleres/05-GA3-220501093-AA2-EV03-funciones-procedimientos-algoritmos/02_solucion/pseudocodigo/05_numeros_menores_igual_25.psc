// GA3-220501093-AA2-EV03
// Problema 5: ingresar 20 numeros y mostrar los menores o iguales a 25.

SubProceso cumple <- EsMenorOIgualAlLimite(numero, limite)
    Definir cumple Como Logico;
    cumple <- numero <= limite;
FinSubProceso

SubProceso EvaluarYMostrar(numero, limite, cantidadMostrada Por Referencia)
    Si EsMenorOIgualAlLimite(numero, limite) Entonces
        Escribir "Valor que cumple: ", numero;
        cantidadMostrada <- cantidadMostrada + 1;
    FinSi
FinSubProceso

Proceso NumerosMenoresOIgualesA25
    Definir numero, limite Como Real;
    Definir posicion, totalDatos, cantidadMostrada Como Entero;

    totalDatos <- 20;
    limite <- 25;
    cantidadMostrada <- 0;

    Para posicion <- 1 Hasta totalDatos Con Paso 1 Hacer
        Escribir "Ingrese el numero ", posicion, " de ", totalDatos, ":";
        Leer numero;
        EvaluarYMostrar(numero, limite, cantidadMostrada);
    FinPara

    Si cantidadMostrada = 0 Entonces
        Escribir "Ningun numero ingresado es menor o igual a 25.";
    SiNo
        Escribir "Cantidad de numeros mostrados: ", cantidadMostrada;
    FinSi
FinProceso
