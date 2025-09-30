# Ejercicio 10.3: Tarea con la clase persona
# Tarea: crear tres objetos más, utilizando los métodos getter and setter
# para modificar, y mostrar los cambios con el método mostrar_detalles()

from Persona2 import Persona2 # Importamos la clase Persona2.


if __name__ == '__main__': # Comprobación del método principal o main.
    persona1 = Persona2('Federico', 'Giglio', 33)
    print(f'Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}') #Llamamos al Método get para cada atributo
    persona1.nombre = 'Raul' #Llamamos al Método set para modificar cada atributo.
    persona1.apellido = 'Orozco'
    persona1.edad = 47
    persona1.mostrar_detalles() # Mostramos las modificaciones realizadas con el método set, llamando al método mostrar_detalles()

    persona2 = Persona2('Marco', 'Segui', 35)
    print(f'Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}') 
    persona2.nombre = 'Tito' 
    persona2.apellido = 'Puente'
    persona2.edad = 76
    persona2.mostrar_detalles()

    persona3 = Persona2('Belén', 'Beningazza', 30)
    print(f'Nombre: {persona3.nombre}, Apellido: {persona3.apellido}, Edad: {persona3.edad}')
    persona3.nombre = 'Janis'
    persona3.apellido = 'Joplin'
    persona3.edad = 27
    persona3.mostrar_detalles() 

    print(__name__)