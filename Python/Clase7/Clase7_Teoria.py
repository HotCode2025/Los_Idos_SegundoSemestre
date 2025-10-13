## Clase7_Python_Teoria
##Programación Orientada a Objetos  (POO)

#Creación de una clase

class Persona: #Creamos una clase
   
    # init es un MÉTODO, lo que está dentro son sus atributos,
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Self se asigna por default y es la referencia al objeto. Este es el método Init Dunder
      self.nombre = nombre         #Creamos una variable nombre que se pasará como parámetro. Antes, valor hardcodeado: 'Juan'
      self.apellido = apellido
      self._dni = dni  #Este atributo está encapsulado. (guión bajo)     
      self.edad = edad     
      self.args = args
      self.kwargs  = kwargs

    def mostrar_detalle(self):
       print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad} la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


print(Persona)

##Objeto persona1 
persona1 = Persona('Nicolas', 'Giglio', 323232921, 37) #No pasamos ninguna referencia. Es una instancia que referencia al constructor (init) de manera indirecta.
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto 1 de la clase Persona: {persona1.nombre}, {persona1.apellido}, y su edad es: {persona1.edad}') #Tarea: imprimir en una linea.

##Objeto persona2
persona2 = Persona('Federico', 'Giglio', 32331123, 33)
print(f'El objeto 2 de la clase Persona: {persona2.nombre}, {persona2.apellido}, y su edad es {persona2.edad}')


#Modificando los atributos de un objeto

persona1.nombre = 'Tito'
persona1.apellido = 'Puente'
persona1.edad = 70

print(f'El objeto 1 tiene ahora los siguientes atributos: nombre: {persona1.nombre}, apellido: {persona1.apellido}, edad: {persona1.edad}')

#Recordar:
## Los atributos son las CARACTERÍSTICAS que va a tener un objeto.
## Los métodos son las ACCIONES que van a ejecutar los objetos. (comportamiento)

persona1.mostrar_detalle() #Llamamos al método "mostrar_detalle" dentro del objeto (creado en lin 13)

persona2.mostrar_detalle() #La referencia en este caso se pasa de manera automática

# Persona.mostrar_detalle(persona1) # Si usamos directamente la Clase para llamar al método HAY QUE PASARLE REFERENCIAS (aquí el objeto). NO se suele USAR ASI

#Creando atributos DENTRO DE UN OBJETO (atributo "superficial", ÚNICO para cada objeto)

persona1.telefono = '333322123'
print(f'Este es el teléfono de: {persona1.nombre}+{persona1.telefono}')
#print(persona2.telefono) => En este caso daría error porque el atributo teléfono no existe en persona2, solo en el objeto persona1

persona3 = Persona('Rogelio', 'Romero', 24112321, 22, 'Teléfono', '2615436521', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen',Modelo=2021)
print(persona3.mostrar_detalle())

persona4 = Persona('Salvador', 'Dali', 72344123, 75, 'Teléfono', '261232323', 'Calle Dominguez', 762, 'Manzana', 88, 'Casa', 19, Altura=1.73, Peso=69, CFavorito='Rojo', Auto='Mercedes', modelo=1975)
print(persona4.mostrar_detalle())
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar en Pyuthon (está encapsulado), esto dice que desconocemos Python.

#persona3.__nombre