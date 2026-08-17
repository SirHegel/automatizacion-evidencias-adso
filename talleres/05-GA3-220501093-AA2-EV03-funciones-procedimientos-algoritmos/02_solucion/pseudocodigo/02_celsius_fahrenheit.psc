// GA3-220501093-AA2-EV03
// Problema 2: convertir una temperatura de grados Celsius a Fahrenheit.

SubProceso fahrenheit <- ConvertirCelsiusAFahrenheit(celsius)
    Definir fahrenheit Como Real;
    fahrenheit <- (9.0 / 5.0) * celsius + 32;
FinSubProceso

SubProceso MostrarConversion(celsius, fahrenheit)
    Escribir celsius, " grados Celsius equivalen a ", fahrenheit, " grados Fahrenheit.";
FinSubProceso

Proceso CelsiusAFahrenheit
    Definir celsius, fahrenheit Como Real;

    Escribir "Ingrese la temperatura en grados Celsius:";
    Leer celsius;

    fahrenheit <- ConvertirCelsiusAFahrenheit(celsius);
    MostrarConversion(celsius, fahrenheit);
FinProceso
