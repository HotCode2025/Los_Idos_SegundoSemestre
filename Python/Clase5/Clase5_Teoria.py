## Clase5_Python_Teoria
## Comenzamos con funciones
# mifuncion() #No se puede llamar antes de definir a una función.

#Definimos una función:
def mi_funcion(): #Para identificar a la función usamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() #Estamos llamando a la función
mi_funcion() #Se puede llamar a ua función N cantidad de veces.

# Desempaquetado de listas oi list Unpacking.
def show(name,lastName):
    print(name + ' ' + lastName)
person = ['Nicolas', 'Giglio']
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la función.
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto

person2 = ("Roberto", "Giordano") # Desempaquetamos a través de una tupla
show(*person2)

person3 = {"lastName": "Giglio", "name": "Federico"}
show(**person3)

## Repaso del ciclo For Else
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3: #Esta es la unica manera para que no se ejecute el Else.
        break
else:
    print("Esto se terminó")

# List comprehension, lista de comprensión:
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista.
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (Funciones)
def mi_funcion2(name, lastName):
    print("Saludos a la gente de Argentina")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2("Jorge", "Lopez")
mi_funcion2("Tito", "Puente")
mi_funcion2("Rafael", "Benitez")

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
resultado = sumar(5, 6)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

# Valores por default en una función
def sumar2(a = 0, b = 0): #Valor por default = 0.
    return(a + b)
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #De esta forma los argumentos son variables. Normalmente se utiliza: *args
    for nombre in nombres: #Se va a convertir en una tupla.
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'María')
listarNombres('Marcos', 'Daniel', 'Romina','Pepe')

#Argumentos variables, diccionarios.
def listarTerminos(**terminos): #Para utilizar argumentos variables se suele usar **kwargs (keyword arguments).
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
listarTerminos() #No recibe argumentos, no muestra nada.
listarTerminos(IDE = 'Integrated Development Environment', PK = 'Primary Key') #Las keys no llevan comillas.
listarTerminos(Nombre = 'Lionel Messi') #Si paso un valor numérico no lo toma.

# Lista de elementos con funciones (convertir)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10) Con un int nos da error porque no es un objeto iterable.
desplegarNombres((10, 11)) #Convertimos a una tupla y lo iteramos. Recordar la coma si es un solo elemento.
desplegarNombres([12, 13]) #Convertimos en una lista y lo iteramos.

# Funciones Recursivas
def factorial(numero):
    if numero == 1: #Caso base.
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo.

resultado = factorial(5)
print(f'El factorial del número 5 es {resultado}')

# Tarea: Solicitar al usuario un número para calcular el factorial:
ingresoUsuario = int(input("Ingrese un número para conocer su factorial: "))
resultado = factorial(ingresoUsuario)
print(f'El resultado del factorial de {ingresoUsuario} es: {resultado}')