#2.1 TIPO SET O CONJUNTO: No tiene un orden,no se puede modificar, si se puede agregar o eliminar, el orden es aleatorio
 
planetas = {'Marte','Júpiter', 'venus'}
print(len(planetas))#Nos muestra la cantidad de elementos
print(planetas)

#Revisar si un elemento existe dentro de set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra') #add es una función, se agrega en forma aleatoria, y no se pueden duplicar
print(planetas)

#La colección de tipo set nos puede servir para evitar elementos duplicados en una lista de datos
#Por ejemplo: DNI, NOMBRE, APELLIDO, MATRICULA DE AUTO, ETC


#Eliminar elementos, puede dar error si el elemento no existe:
planetas.remove('Júpiter')#Está funcion ante un mal ingreso u inexistencia da error
print(planetas)
planetas.discard('tierra') #Está funcion no nos presenta ningun error, el set no sufre modificaciones.
print(planetas)


#limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
#print(planetas)


#2.2 DICCIONARIO EN PYTHON

#'Maradona': 10 Un diccionario esta compuesto por dos elementos
#Una llave (Key) y un valor (Value)
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POO': 'Programacion Orientada a objetos',
    'SABD': 'Sistema de administracion de Base de Datos'

}
print(len(diccionario))#Cantidad de elementos
print(diccionario)

#Acceder a un diccionario con la key
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos los elemetentos
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

#Como recorrer los elementos
for termino in diccionario: #Solo accedemos a las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)


#Otras maneras de acceder a un diccionario
for termino in diccionario. keys():
    print(termino) #Muestra solo las llaves

for valor in diccionario.values(): #Usamos la funcion para acceder al valor
    print(valor)


#Comprobar la existencia de algun elemento
print('IDE' in diccionario) #Devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario

# Concatenamos lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para saber el indice de un elemento

#Como saber cuantos valores repetidos hay dentro de la lista
print(lista3.count(1))

#Para poner al reves una lista
lista3.reverse()
print(lista3)


#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)
lista = lista3 * 2
print(lista)

#Metodos de ordenamiento
lista3.sort() #Ordena los elementos en forma ascendente
print(lista3)

lista3.sort(reverse=True)
print(lista3)

#Repaso de tuplas
tupla = (4, 'hola', 6.78, [1, 2, 78], 4, 'Hola') #Se puede tener diferentes tipos de datos dentro de una tupla 
print(tupla)

#Buscando elementos
print(4 in tupla) #Respuesta booleana

#Lo que podemos usar dentro de tuplas son: Index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla
