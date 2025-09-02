#Ejericio2:Operaciones de conjunto con listas. Escriba un programa que tenga 2 listas y que a continuación cree las siguientes listas (en las que no debe haber repetición) :
#1. Lista de palabras que aparecen en las listas.
#2. Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#3. Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#4. Lista de palabras que aparecen en ambas listas.


# Definimos dos listas con diferentes leguajes de programación.
lista1 = ["python", "java", "c++", "javascript", "python", "html"]
lista2 = ["java", "python", "ruby", "css", "javascript", "php"]

# 1- Lista de palabras que aparecen en las listas 
todasPalabras = list(set(lista1) | set(lista2))

# 2- Lista de palabras que aparecen en la primera lista pero no en la segunda
soloLista1 = list(set(lista1) - set(lista2))

# 3- Lista de palabras que aparecen en la segunda lista pero no en la primera
soloLista2 = list(set(lista2) - set(lista1))

# 4- Lista de palabras que aparecen en ambas listas (intersección)
ambasListas = list(set(lista1) & set(lista2))

# Mostrar los resultados de las listas pedidas
print("Lista 1:", lista1) 
print("Lista 2:", lista2) 
print("\n1. Palabras que aparecen en las listas:", sorted(todasPalabras)) 
print("2. Palabras solo en la primera lista:", sorted(soloLista1)) 
print("3. Palabras solo en la segunda lista:", sorted(soloLista2)) 
print("4. Palabras en ambas listas:", sorted(ambasListas)) 