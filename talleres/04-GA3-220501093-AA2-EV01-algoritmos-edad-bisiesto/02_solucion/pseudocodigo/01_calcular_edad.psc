// GA3-220501093-AA2-EV01
// Algoritmo 1: calcular la edad actual en años cumplidos.

SubProceso bisiesto <- EsBisiesto(anio)
    Definir bisiesto Como Logico;
    bisiesto <- (anio MOD 400 = 0) O ((anio MOD 4 = 0) Y (anio MOD 100 <> 0));
FinSubProceso

SubProceso valida <- FechaValida(dia, mes, anio)
    Definir limite Como Entero;
    Definir valida Como Logico;
    valida <- Falso;

    Si anio > 0 Y mes >= 1 Y mes <= 12 Entonces
        Segun mes Hacer
            1, 3, 5, 7, 8, 10, 12:
                limite <- 31;
            4, 6, 9, 11:
                limite <- 30;
            2:
                Si EsBisiesto(anio) Entonces
                    limite <- 29;
                SiNo
                    limite <- 28;
                FinSi
        FinSegun
        valida <- dia >= 1 Y dia <= limite;
    FinSi
FinSubProceso

SubProceso ordenValido <- NoEsPosterior(dia1, mes1, anio1, dia2, mes2, anio2)
    Definir ordenValido Como Logico;
    ordenValido <- (anio1 < anio2) O ((anio1 = anio2) Y ((mes1 < mes2) O ((mes1 = mes2) Y (dia1 <= dia2))));
FinSubProceso

Proceso CalcularEdadActual
    Definir diaNacimiento, mesNacimiento, anioNacimiento Como Entero;
    Definir diaActual, mesActual, anioActual, edad Como Entero;
    Definir datosValidos Como Logico;
    Definir continuar Como Caracter;

    continuar <- "S";
    Mientras Mayusculas(continuar) = "S" Hacer
        Repetir
            Escribir "Fecha de nacimiento (dia mes anio):";
            Leer diaNacimiento, mesNacimiento, anioNacimiento;
            Escribir "Fecha actual (dia mes anio):";
            Leer diaActual, mesActual, anioActual;

            datosValidos <- FechaValida(diaNacimiento, mesNacimiento, anioNacimiento) Y FechaValida(diaActual, mesActual, anioActual);
            Si datosValidos Entonces
                datosValidos <- NoEsPosterior(diaNacimiento, mesNacimiento, anioNacimiento, diaActual, mesActual, anioActual);
            FinSi

            Si NO datosValidos Entonces
                Escribir "Datos invalidos: revise las fechas y su orden.";
            FinSi
        Hasta Que datosValidos

        edad <- anioActual - anioNacimiento;
        Si (mesActual < mesNacimiento) O ((mesActual = mesNacimiento) Y (diaActual < diaNacimiento)) Entonces
            edad <- edad - 1;
        FinSi

        Escribir "Edad actual: ", edad, " anios cumplidos.";

        Repetir
            Escribir "¿Desea procesar otro caso? (S/N):";
            Leer continuar;
            continuar <- Mayusculas(continuar);
        Hasta Que continuar = "S" O continuar = "N"
    FinMientras
FinProceso
