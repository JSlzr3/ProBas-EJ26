# Problema 41 Confirmación de contraseña sin límite
password = input("Crea tu contraseña: ")
confirmacion = input("Confirma la contraseña: ")

while confirmacion != password:
    print("No coinciden.")
    confirmacion = input("Confirma nuevamente: ")

print("Contraseña confirmada.")
