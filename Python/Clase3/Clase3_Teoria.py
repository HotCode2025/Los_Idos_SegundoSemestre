# Clase_3_Python_Teoria

# REPASO DE CONJUNTOS O SETS

## Recordamos que los conjuntos son grupos de elementos desordenados con valores únicos.

## Para definir un conjunto

conjunto2 = set() # Esto inicializa un conjunto vacío (con set())
conjunto1 = {'bye', } #Esto inicializa un conjunto con llaves. SI o SI tiene que tener un elemento de esta forma.
conjunto2.add(7) #Funcion .add() para añadir elementos al conjunto. Solo puedo ingresar de a 1 elemento.
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) #Devuelve un bool como respueta.

##Cómo hacer la igualdad entre conjuntos:
print(conjunto1 == conjunto2) #Devuelve un booleano como respuesta.

## OPERACIONES CON CONJUNTOS

## Union de Conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea indica "unión". Muestra TODOS los elementos de ambos conj.
print(conjunto3) # Nota, si hubiera añadido 'Hola' (con mayusc) en la línea 13, no hubiera aparecido en el print sino que aparecería una sola vez (Duplic).

conjunto3 = conjunto1 & conjunto2 # Guarda los elementos EN COMÚN entre los conjuntos.
print(conjunto3)

conjunto3 = conjunto2 - conjunto1 # Asigna el valor que está en el conjunto1 y NO en el conjunto2
print(conjunto3) 

conjunto3 = conjunto1 ^ conjunto2 # Elementos que NO COMPARTEN o que son DIFERENTES entre ambos conjuntos. (diferencia simétrica). 
print(conjunto3)

## Como determinar si un conjunto es subconjunto de otro
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aquí comprobamos si un conj es subconj de otro (usando .issubset()) -True
print(conjunto2.issubset(conjunto1)) # -False

## Como determinar si un conjunto es un superconjunto (lo integran otros)
print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 están dentro del conjunto3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el cnunto3 es un superconjunto.
print(conjunto2.issuperset(conjunto3))

## Como determinar si ambos conjuntos son disconexos, esto es si no comparten elementos en comun.
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

## Cómo convertir un conjunto para que sea totalmente inmutable.
conjunto1 = frozenset # Esto "congela" el conjunto haciéndolo inmutable. No se puede agregar, modificar ni eliminar elementos del conjunto.


# REPASO DE DICCIONARIOS

## Creamos un diccionario

diccionarioNuevo = {'Azul': 'Blue', 'Rojo':'Red', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

## Como eliminar una key/value determinada

del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

## Los diccionarios pueden almacenar diferente tipo de datos
diccionario2 = {'Nicolas': {'Edad': 37, 'Altura': 1.81}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)


#  MÉTODO CON LISTAS: PILAS

## Pilas usando listas
pila = [1, 2, 3]
print(pila)

## Funcion append(valor): Agregar elementos a la pila por el final de la misma (luege del último elemento)
pila.append(4)
pila.append(5)
print(pila)

## Funcion pop(): Quitar elementos desde el final.

elementoBorrado = pila.pop() #Quita el último elemento y lo guarda en la variable
print(pila)
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedó con los siguientes elementos: {pila}')

# MÉTODOS CON LISTAS: COLAS

## Estructura de datos de tipo "fifo" (first in / first out)
cola = ['Nicolas','Federico', 'Belén', 'Marco']

## Agregamos elementos al final de la cola
cola.append('Magui')
cola.append('Gabi')
print(cola)

## Quitamos elementos de la cola
seRetira = cola.pop(0)
print(f' Atendido: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f' Atendido: {seRetira}')
print(cola)    