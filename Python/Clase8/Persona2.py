class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}')
    
    @property # Decorador
    def nombre(self): # Método Getter
        #print ('Estamos utilizando el método get')
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): # Método Setter
        #print ('Estamos utilizando el método set')
        self._nombre = nombre

    @property # Decorador
    def apellido(self): # Método Getter
        #print ('Estamos utilizando el método get')
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido): # Método Setter
        #print ('Estamos utilizando el método set')
        self._apellido = apellido

    @property # Decorador
    def edad(self): # Método Getter
        #print ('Estamos utilizando el método get')
        return self._edad
    
    @edad.setter
    def edad(self, edad): # Método Setter
        #print ('Estamos utilizando el método set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')



if __name__ == '__main__':
    persona1 = Persona2('Nicolas', 'Giglio', '38')
    print(persona1.nombre) # Llamamos al método Getter.
    persona1.nombre = 'Juan Pedro' # Aquí llama al método Setter.
    print(persona1.nombre) # Aquí volvemos a llamar al método Getter.
    print(persona1.mostrar_detalles())
    # Atributo read-only, sería la edad porque no tiene método set (si comentamos el bloque 35-38)
    print(persona1.edad)
    print(__name__)