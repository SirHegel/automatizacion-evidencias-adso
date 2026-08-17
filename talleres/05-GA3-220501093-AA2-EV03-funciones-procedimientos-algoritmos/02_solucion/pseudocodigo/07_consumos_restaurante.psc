// GA3-220501093-AA2-EV03
// Problema 7: calcular los pagos de clientes de un restaurante.
// El descuento del 20 % se aplica solo cuando el consumo excede 50000.

SubProceso valido <- ConsumoValido(consumo)
    Definir valido Como Logico;
    valido <- consumo >= 0;
FinSubProceso

SubProceso pago <- CalcularPago(consumo)
    Definir pago Como Real;

    Si consumo > 50000 Entonces
        pago <- consumo * 0.80;
    SiNo
        pago <- consumo;
    FinSi
FinSubProceso

SubProceso LeerConsumoValido(numeroCliente, consumo Por Referencia)
    Repetir
        Escribir "Ingrese el consumo del cliente ", numeroCliente, ":";
        Leer consumo;
        Si NO ConsumoValido(consumo) Entonces
            Escribir "Consumo invalido. No puede ser negativo.";
        FinSi
    Hasta Que ConsumoValido(consumo)
FinSubProceso

Proceso ConsumosRestaurante
    Definir cantidadClientes, cliente Como Entero;
    Definir consumo, pago, totalPagos Como Real;

    Repetir
        Escribir "Ingrese la cantidad de clientes, mayor que cero:";
        Leer cantidadClientes;
        Si cantidadClientes <= 0 Entonces
            Escribir "Cantidad invalida. Debe existir al menos un cliente.";
        FinSi
    Hasta Que cantidadClientes > 0

    totalPagos <- 0;
    Para cliente <- 1 Hasta cantidadClientes Con Paso 1 Hacer
        LeerConsumoValido(cliente, consumo);
        pago <- CalcularPago(consumo);
        totalPagos <- totalPagos + pago;

        Si consumo > 50000 Entonces
            Escribir "Cliente ", cliente, ": pago con descuento = ", Redon(pago * 100) / 100;
        SiNo
            Escribir "Cliente ", cliente, ": pago sin descuento = ", Redon(pago * 100) / 100;
        FinSi
    FinPara

    Escribir "Total de todos los pagos: ", Redon(totalPagos * 100) / 100;
FinProceso
