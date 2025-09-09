## Clase5_Ejercicio1_Python.
# "Ejercicio 11": Agenda telefónica.
# Hacer un programa que simule una agenda de contactos. Crear
# un diccionario donde la clave sea el nombre del usuario y el valor 
# sea el teléfono. El programa tendrá el siguiente menú de opciones:
#   1. Nuevo contacto.
#   2. Borrar contacto.
#   3. Ver contactos existentes.
#   4. Salir.

agenda = {}

while True:
    print("\n--- Agenda Telefónica - Menú ---")
    print("Opción 1: Nuevo Contacto")
    print("Opción 2: Borrar Contacto")
    print("Opción 3: Ver Contactos Existentes")
    print("Opción 4: Salir")

    opcion = input("Digite la opción deseada (1-4): ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        if nombre in agenda:
            print("Advertencia: El contacto ya existe.")
        else:
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono;
    elif opcion == "2":
        nombre = input("Nombre del contacto a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("El contacto ha sido eliminado.")
        else:
            print("El contacto no existe.")
    elif opcion == "3":
        if agenda:
            print("\n Contactos en la agenda: ")
            for nombre, telefono in agenda.items():
                print(f" {nombre}: {telefono}")
        else:
            print("La agenda está vacía.")
    elif opcion == "4":
        print("Saliendo de la agenda.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")