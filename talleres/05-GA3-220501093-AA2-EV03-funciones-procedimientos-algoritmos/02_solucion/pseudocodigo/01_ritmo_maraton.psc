// GA3-220501093-AA2-EV03
// Problema 1: calcular el ritmo medio de un maraton de 42.195 km
// recorrido en 2 horas y 25 minutos.

SubProceso valido <- DatosMaratonValidos(distancia, horas, minutos)
    Definir valido Como Logico;
    valido <- distancia > 0 Y horas >= 0 Y minutos >= 0 Y minutos < 60 Y (horas > 0 O minutos > 0);
FinSubProceso

SubProceso ritmo <- CalcularRitmoMinutosPorKilometro(distancia, horas, minutos)
    Definir ritmo, tiempoTotalMinutos Como Real;
    tiempoTotalMinutos <- horas * 60 + minutos;
    ritmo <- tiempoTotalMinutos / distancia;
FinSubProceso

SubProceso MostrarRitmo(ritmo)
    Definir minutosEnteros Como Entero;
    Definir segundos Como Real;

    minutosEnteros <- Trunc(ritmo);
    segundos <- Redon((ritmo - minutosEnteros) * 60 * 100) / 100;

    // Se normaliza un posible redondeo de 60 segundos.
    Si segundos >= 60 Entonces
        minutosEnteros <- minutosEnteros + 1;
        segundos <- 0;
    FinSi

    Escribir "Ritmo medio: ", ritmo, " minutos por kilometro.";
    Escribir "Equivale a ", minutosEnteros, " minutos y ", segundos, " segundos por kilometro.";
FinSubProceso

Proceso RitmoMaraton
    Definir distancia, ritmo Como Real;
    Definir horas, minutos Como Entero;

    Repetir
        Escribir "Ingrese la distancia recorrida en kilometros:";
        Leer distancia;
        Escribir "Ingrese las horas y los minutos empleados:";
        Leer horas, minutos;

        Si NO DatosMaratonValidos(distancia, horas, minutos) Entonces
            Escribir "Datos invalidos. Revise la distancia y el tiempo.";
        FinSi
    Hasta Que DatosMaratonValidos(distancia, horas, minutos)

    ritmo <- CalcularRitmoMinutosPorKilometro(distancia, horas, minutos);
    MostrarRitmo(ritmo);
FinProceso
