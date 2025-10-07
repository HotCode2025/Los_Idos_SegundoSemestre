# Ejercicio 11.3 - Clase Persona #
#Tarea: Encapsular los atributos y agregar los método getters and setters
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): #Sobreescribir
        return f'Persona: [ Nombre: {self._nombre}, Edad: {self._edad}]'

class Empleado(Persona):    #Esta clase es hija de la clase Persona.
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
        
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}'

empleado1 = Empleado('Tito', 75000, 38)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)