# Problema 42 Confirmación de contraseña con límite
password = input("Crea tu contraseña: ")
intentos = 3

while intentos > 0:
    confirmacion = input("Confirma la contraseña: ")

    if confirmacion == password:
        print("Contraseña confirmada.")
        break
    else:
        intentos -= 1
        print("No coinciden. Intentos restantes:", intentos)

if intentos == 0:
    print("Cuenta cancelada")
