# Problema 38 Validación de número entre 1 y 5
numero = int(input("Ingresa un número entre 1 y 5: "))

while numero < 1 or numero > 5:
    print("Número fuera de rango.")
    numero = int(input("Intenta nuevamente: "))

print("Número válido:", numero)
