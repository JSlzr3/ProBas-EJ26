# Problema 36 Repetir elevación al cuadrado
respuesta = "si"

while respuesta.lower() == "si":
    numero = float(input("Ingresa un número: "))
    print("Su cuadrado es:", numero ** 2)
    respuesta = input("¿Deseas ingresar otro número? (si/no): ")
