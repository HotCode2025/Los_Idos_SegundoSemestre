
#Lista = Ariel , Liliana , Natalia, Osvaldo

nombres = ['Naty','Osvaldo', 'Lily','Ariel']
print(nombres)
print(nombres[0]) #Mostramos el primer elemento de la lista
print(nombres[1])#Mostramos el segundo elemento de la lista

#Mostramos elementos de manera inversa
print(nombres[3]) #Usamos el ultimo elemento de la lista
print(nombres[-1])#Usamos numero negativos


#Recuperar un rango de la lista
print(nombres[0:2])#Solo muestrael indica 0 y 1, pero no el índice 2.

#Ir del inicio de la lista al indice(sin incluirlo)
print(nombres[ : 3])

#Desde el indice indicado hasta el final
print(nombres[1 : ])

#Modificamos un valor:
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural.
    print(nombre)
else:
    print('Se acabaron los nombres de la lista')


#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos como parametros la lista

#Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

#Agregamos un elemento de un índice específico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()#Ultimo elemento de la lista
print(nombres)

#Eliminamos un indice especifico
del nombres[2] #Se elimina el indice 2
print(nombres)

#Eliminar, borrar o limpiar todos los elentos
nombres.clear()
print(nombres)

#Eliminar lista
del nombres
print(nombres)
