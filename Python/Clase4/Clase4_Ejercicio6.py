# Clase4_Ejercicio6_Python: "Insertar elementos y ordenarlos"
## Ejercicio: Pedir números y meterlos en una lista, cuando el usuario
## introduzca un número 0, nuestro programa dejaría de insertar.
## Por último, mostrar los números ordenados de menor a mayor.

lista = []
ingresoUsuario = int(input("Por favor ingrese un número a la lista ditinto de 0: "))
while (ingresoUsuario != 0):
    lista.append(ingresoUsuario)
    ingresoUsuario = int(input("Por favor otro número a la lista ditinto de 0: "))
print("El programa ha finalizado por ingresar 0")
print(f"La lista ordenada con los valores de menor a mayor es: {sorted(lista)}")

