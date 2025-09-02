#Ejercicio 4: Llenar una lista. Llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for, 
#los elementos deben mostrarse de la siguiente forma: 1-2-3-4-5...-50

#Lista vacía
lista = []

#Rellenamos la lista con los valores

for i in range(1, 51):
    lista.append(i)

#Ahora mostramos la lista, para eso hacemos un if para saber si el elemento es el último o no de la lista, porque ese no lleva guión
for i in range(len(lista)):
    if i == len(lista) - 1:
        print(lista[i]) #acá printeamos el último valor
    else:
        print(lista[i], end="-") #acá printeamos los demás valores para que se muestren con guión y no coma


