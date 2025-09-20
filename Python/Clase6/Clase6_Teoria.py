## Clase6_Python_Teoria
##Programación Orientada a Objetos  (POO)

#Creación de una clase

class Persona: #Creamos una clase
   
    # init es un MÉTODO, lo que está dentro son sus atributos,
    def __init__(self, nombre, apellido, edad): #Self se asigna por default y es la referencia al objeto. #Luego se le pasan los parámetros (ver lin 9-11)
      self.nombre = nombre         #Creamos una variable nombre que se pasará como parámetro. Antes, valor hardcodeado: 'Juan'
      self.apellido = apellido       #Creamos una variable apellido que se pasará como parámetro.  Antes, valor harcodeado: 'Perez'
      self.edad = edad         #Creamos una variable edad que se pasará como parámetro. Antes, valor harcodeado: 22
    def mostrar_detalle(self):
       print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


print(Persona)

##Objeto persona1 
persona1 = Persona('Nicolas', 'Giglio', 37) #No pasamos ninguna referencia. Es una instancia que referencia al constructor (init) de manera indirecta.
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto 1 de la clase Persona: {persona1.nombre}, {persona1.apellido}, y su edad es: {persona1.edad}') #Tarea: imprimir en una linea.

##Objeto persona2
persona2 = Persona('Federico', 'Giglio', 33)
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
persona2.mostrar_detalle()