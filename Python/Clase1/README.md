# 1.1 listas parte 1
#lista = Ariel, Liliana, Natalia, Osvaldo
nombres = ["Naty","Osvaldo","Lily","Ariel"]
print(nombres)
print (nombres[0])
print (nombres[1])
print (nombres [-1])
print(nombres [-2])


# 1.1 listas parte 2
print(nombres)
print(nombres[0:2])# solo muestra el indice 0,1 pero no el indice 2
#ir de inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])#indices a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[3] ="Liliana"
nombres[0] = "Natalia"
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")


# 1.1 Listas Parte 3
#Preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

#Agregar elementos 
nombres.append("Marcelo")
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

#Eliminar un elemento
nombres.remove("Alberto")
print(nombres)

#Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #delete = eliminar
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar lista
del nombres
print(nombres) #Aqui mostrará un error porque la lista se eliminó y interpreta que "nombre" no esta definida