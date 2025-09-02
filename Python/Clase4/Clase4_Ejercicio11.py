# Ejercicio 8: Menu interactivo - cajero automatico
# Hacer un programa que simule un cajero automatico
# con un saldo inicial de $1000 con el siguiente menu de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo_inicial = 1000

while True:
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Opción 1: Ingresar dinero
        ingreso = float(input("Introduce la cantidad a ingresar: "))
        if ingreso > 0:
            saldo_inicial += ingreso
            print(f"Has ingresado ${ingreso} en tu cuenta.")
        else:
            print("Cantidad inválida. El ingreso debe ser mayor a 0.")

    elif opcion == "2":
        # Opción 2: Retirar dinero
        retiro = float(input("Introduce la cantidad a retirar: "))
        if retiro > 0 and retiro <= saldo_inicial:
            saldo_inicial -= retiro
            print(f"Has retirado ${retiro} de tu cuenta.")
        elif retiro > saldo_inicial:
            print("Saldo insuficiente.")
        else:
            print("Cantidad no válida. El retiro debe ser mayor a 0.")

    elif opcion == "3":
        # Opción 3: Mostrar saldo disponible
        print(f"Tu saldo actual es de ${saldo_inicial}")

    elif opcion == "4":
        # Opción 4: Salir del programa
        print("Gracias por elegirnos")
        break

    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.") #Si usuario elige un numero fuera del menu disponible