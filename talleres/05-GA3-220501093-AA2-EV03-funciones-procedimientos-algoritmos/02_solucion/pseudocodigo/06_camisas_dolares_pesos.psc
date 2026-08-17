// GA3-220501093-AA2-EV03
// Problema 6: sumar cinco precios de camisas en dolares y convertir el total a pesos.
// La tasa de cambio se solicita como entrada para no depender de un valor desactualizado.

SubProceso valido <- PrecioValido(precio)
    Definir valido Como Logico;
    valido <- precio >= 0;
FinSubProceso

SubProceso LeerPrecioValido(posicion, precio Por Referencia)
    Repetir
        Escribir "Ingrese el precio en dolares de la camisa ", posicion, ":";
        Leer precio;
        Si NO PrecioValido(precio) Entonces
            Escribir "Precio invalido. No puede ser negativo.";
        FinSi
    Hasta Que PrecioValido(precio)
FinSubProceso

SubProceso totalPesos <- ConvertirDolaresAPesos(totalDolares, tasaCambio)
    Definir totalPesos Como Real;
    totalPesos <- totalDolares * tasaCambio;
FinSubProceso

Proceso CamisasDolaresAPesos
    Definir precio, totalDolares, tasaCambio, totalPesos Como Real;
    Definir posicion Como Entero;

    Repetir
        Escribir "Ingrese cuantos pesos equivalen a un dolar:";
        Leer tasaCambio;
        Si tasaCambio <= 0 Entonces
            Escribir "Tasa invalida. Debe ser mayor que cero.";
        FinSi
    Hasta Que tasaCambio > 0

    totalDolares <- 0;
    Para posicion <- 1 Hasta 5 Con Paso 1 Hacer
        LeerPrecioValido(posicion, precio);
        totalDolares <- totalDolares + precio;
    FinPara

    totalPesos <- ConvertirDolaresAPesos(totalDolares, tasaCambio);
    Escribir "Total en dolares: USD ", Redon(totalDolares * 100) / 100;
    Escribir "Total en pesos: COP ", Redon(totalPesos * 100) / 100;
FinProceso
