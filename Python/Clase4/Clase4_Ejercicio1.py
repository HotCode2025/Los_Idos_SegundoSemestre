#Ejercicio 1: Eliminar duplicados de una lista. Escriba un programa donde tenga una lista
#y que a continuación elimine los elementos repetidos, por último mostrar la lista.

#Creamos la lista original.
lista_original = [1, 2, 3, 2, 4, 1, 5, 4, 3, 5, 6]
lista_sin_duplicados = []

#Recorremos la lista original con un ciclo For. 

for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

#Mostramos en pantalla las listas con duplicados y la lista con elementos eliminados.

print('La lista original es:', lista_original)
print('La lista sin duplicados es:', lista_sin_duplicados)