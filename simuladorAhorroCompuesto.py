# Simulador de ahorro con interes compuesto

MAX_MESES = 120

ahorro_inicial = float(input("Ingrese el ahorro inicial en colones: ₡"))
aporte_mensual = float(input("Ingrese el aporte mensual en colones: ₡"))
tasa_interes = float(input("Ingrese la tasa de interes mensual (%): "))
meta_ahorro = float(input("Ingrese la meta de ahorro en colones: ₡"))

saldo = ahorro_inicial
mes = 0

print("\n--- Evolucion del ahorro ---")

while saldo < meta_ahorro and mes < MAX_MESES:

    interes = saldo * tasa_interes / 100

    saldo = saldo + interes

    saldo = saldo + aporte_mensual

    mes = mes + 1

    print("Mes", mes, ": saldo = ₡", round(saldo, 2))

if saldo >= meta_ahorro:
    print("Meta de ahorro alcanzada")
    print("Mes en que se alcanzo:", mes)
    print("Saldo final: ₡", round(saldo, 2))

else:
    faltante = meta_ahorro - saldo

    print("\nSe alcanzo el limite de", MAX_MESES, "meses.")
    print("Saldo final: colones", round(saldo, 2))
    print("Dinero que falta para la meta: ₡", round(faltante, 2))