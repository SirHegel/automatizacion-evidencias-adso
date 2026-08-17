// GA3-220501093-AA2-EV01
// Algoritmo 2: determinar si un año gregoriano es bisiesto.

Proceso DeterminarAnioBisiesto
    Definir anio, residuo4, residuo100, residuo400 Como Entero;
    Definir bisiesto Como Logico;
    Definir continuar Como Caracter;

    continuar <- "S";
    Mientras Mayusculas(continuar) = "S" Hacer
        Repetir
            Escribir "Ingrese un anio positivo:";
            Leer anio;
            Si anio <= 0 Entonces
                Escribir "Dato invalido: el anio debe ser mayor que cero.";
            FinSi
        Hasta Que anio > 0

        residuo4 <- anio MOD 4;
        residuo100 <- anio MOD 100;
        residuo400 <- anio MOD 400;
        bisiesto <- (residuo400 = 0) O ((residuo4 = 0) Y (residuo100 <> 0));

        Si bisiesto Entonces
            Escribir "El anio ", anio, " es bisiesto.";
        SiNo
            Escribir "El anio ", anio, " no es bisiesto.";
        FinSi

        Repetir
            Escribir "¿Desea evaluar otro anio? (S/N):";
            Leer continuar;
            continuar <- Mayusculas(continuar);
        Hasta Que continuar = "S" O continuar = "N"
    FinMientras
FinProceso
