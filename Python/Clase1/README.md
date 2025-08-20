#1.1 listas parte 1
# lista = Ariel, Liliana, Natalia, Osvaldo
nombres = ["Naty","Osvaldo","Lily","Ariel"]
print(nombres)
print (nombres[0])
print (nombres[1])
print (nombres [-1])
print(nombres [-2])


#1.1 listas parte 2
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