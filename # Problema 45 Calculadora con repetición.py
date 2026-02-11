# Problema 45 Calculadora con repetición por operación
programa = "si"

while programa.lower() == "si":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    op = input("Operación (+ - * / ** %): ")

    repetir_operacion = "si"

    while repetir_operacion.lower() == "si":
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

        repetir_operacion = input("¿Repetir misma operación? (si/no): ")

    programa = input("¿Deseas realizar otra operación distinta? (si/no): ")

print("Calculadora cerrada.")
