# Problema 44 Calculadora básica con repetición
seguir = "si"

while seguir.lower() == "si":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    op = input("Operación (+ - * / ** %): ")

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("No se puede dividir entre 0")
        else:
            print(a / b)
    elif op == "**":
        print(a ** b)
    elif op == "%":
        print(a % b)
    else:
        print("Operación inválida")

    seguir = input("¿Otra operación? (si/no): ")
