# Problema 43 Acumulador de abonos
total = 0

while total <= 100000:
    abono = float(input("¿Cantidad a abonar?: "))

    if abono < 0:
        print("Error: no se aceptan cantidades negativas.")
    else:
        total += abono
        print("Total acumulado:", total)

print("Meta superada.")
