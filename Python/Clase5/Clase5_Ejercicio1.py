## Clase5_Ejercicio1_Python.
# "Ejercicio 10": No repetir caracteres.
# Hacer un programa que pida una cadena por teclado, luego 
# meter los caracteres en una lista sin repetir caracteres.

cadena = input("Digite una palabra: ")
lista=[]

for char in cadena:
    if char not in lista:
        lista.append(char)

print(lista)

