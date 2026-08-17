// GA3-220501093-AA2-EV03
// Problema 3: calcular la nota del primer parcial de analisis.
// Supuesto declarado: las dos notas de taller y el quiz tienen el mismo peso
// dentro del componente de seguimiento, que vale el 30 %.

SubProceso valida <- NotaValida(nota)
    Definir valida Como Logico;
    valida <- nota >= 0 Y nota <= 5;
FinSubProceso

SubProceso notaFinal <- CalcularNotaPrimerParcial(taller1, taller2, quiz, examen)
    Definir promedioSeguimiento, notaFinal Como Real;
    promedioSeguimiento <- (taller1 + taller2 + quiz) / 3;
    notaFinal <- promedioSeguimiento * 0.30 + examen * 0.70;
FinSubProceso

Proceso NotaPrimerParcial
    Definir taller1, taller2, quiz, examen, notaFinal Como Real;

    Repetir
        Escribir "Ingrese las notas de taller 1, taller 2, quiz y examen (0 a 5):";
        Leer taller1, taller2, quiz, examen;

        Si NO NotaValida(taller1) O NO NotaValida(taller2) O NO NotaValida(quiz) O NO NotaValida(examen) Entonces
            Escribir "Notas invalidas. Todas deben estar entre 0 y 5.";
        FinSi
    Hasta Que NotaValida(taller1) Y NotaValida(taller2) Y NotaValida(quiz) Y NotaValida(examen)

    notaFinal <- CalcularNotaPrimerParcial(taller1, taller2, quiz, examen);
    Escribir "Nota del primer parcial: ", Redon(notaFinal * 100) / 100;
FinProceso
