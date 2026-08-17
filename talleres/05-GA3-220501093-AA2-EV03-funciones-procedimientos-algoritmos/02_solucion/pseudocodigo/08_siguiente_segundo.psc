// GA3-220501093-AA2-EV03
// Problema 8: calcular la hora correspondiente al siguiente segundo.

SubProceso valida <- HoraValida(hora, minuto, segundo)
    Definir valida Como Logico;
    valida <- hora >= 0 Y hora <= 23 Y minuto >= 0 Y minuto <= 59 Y segundo >= 0 Y segundo <= 59;
FinSubProceso

SubProceso AvanzarUnSegundo(hora Por Referencia, minuto Por Referencia, segundo Por Referencia)
    segundo <- segundo + 1;

    Si segundo = 60 Entonces
        segundo <- 0;
        minuto <- minuto + 1;

        Si minuto = 60 Entonces
            minuto <- 0;
            hora <- hora + 1;

            Si hora = 24 Entonces
                hora <- 0;
            FinSi
        FinSi
    FinSi
FinSubProceso

Proceso SiguienteSegundo
    Definir hora, minuto, segundo Como Entero;

    Repetir
        Escribir "Ingrese la hora, los minutos y los segundos:";
        Leer hora, minuto, segundo;

        Si NO HoraValida(hora, minuto, segundo) Entonces
            Escribir "Hora invalida. Use H=0..23, M=0..59 y S=0..59.";
        FinSi
    Hasta Que HoraValida(hora, minuto, segundo)

    AvanzarUnSegundo(hora, minuto, segundo);
    Escribir "Hora en el siguiente segundo: ", hora, ":", minuto, ":", segundo;
FinProceso
