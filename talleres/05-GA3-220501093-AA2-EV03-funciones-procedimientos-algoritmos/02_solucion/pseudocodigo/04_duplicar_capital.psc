// GA3-220501093-AA2-EV03
// Problema 4: determinar cuantos anios tarda un capital en duplicarse.
// Supuesto declarado: la tasa se expresa como porcentaje anual y los
// intereses se capitalizan una vez al final de cada anio.

SubProceso valido <- DatosFinancierosValidos(capital, tasaAnual)
    Definir valido Como Logico;
    valido <- capital > 0 Y tasaAnual > 0;
FinSubProceso

SubProceso CalcularDuplicacion(capital, tasaAnual, anios Por Referencia, montoFinal Por Referencia)
    Definir meta Como Real;

    meta <- capital * 2;
    montoFinal <- capital;
    anios <- 0;

    Mientras montoFinal < meta Hacer
        montoFinal <- montoFinal * (1 + tasaAnual / 100);
        anios <- anios + 1;
    FinMientras
FinSubProceso

Proceso DuplicarCapital
    Definir capital, tasaAnual, montoFinal Como Real;
    Definir anios Como Entero;

    Repetir
        Escribir "Ingrese el capital inicial, mayor que cero:";
        Leer capital;
        Escribir "Ingrese la tasa de interes anual en porcentaje, mayor que cero:";
        Leer tasaAnual;

        Si NO DatosFinancierosValidos(capital, tasaAnual) Entonces
            Escribir "Datos invalidos. El capital y la tasa deben ser positivos.";
        FinSi
    Hasta Que DatosFinancierosValidos(capital, tasaAnual)

    CalcularDuplicacion(capital, tasaAnual, anios, montoFinal);
    Escribir "El capital se duplica al terminar el anio ", anios, ".";
    Escribir "Monto alcanzado: ", Redon(montoFinal * 100) / 100;
FinProceso
