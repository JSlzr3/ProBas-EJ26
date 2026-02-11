# Problema 37 Interés compuesto con repetición
resp = "si"

while resp.lower() == "si":
    C = float(input("Capital inicial: "))
    i = float(input("Tasa de interés (ej: 0.05): "))
    n = int(input("Número de periodos: "))

    M = C * (1 + i) ** n
    print("Monto final:", M)

    resp = input("¿Deseas hacer otro cálculo? (si/no): ")
