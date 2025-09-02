# Clase4_Ejercicio5_Python: "Modificar los elementos de una lista"
## Ejercicio: Llenar una lista con los números del 1 al 10, luego modificar los
## elementos de la lista multiplicándolos por un valor ingresado por el usuario.

lista = list(range(1, 11))
for i in range(len(lista)):
    multiplicarPor = int(input(f"Ingrese un número para multiplicar el valor actual '{i+1}': "))
    lista[i] = lista[i]*multiplicarPor

print(f"Los nuevos valores de la lista son: {lista}")

