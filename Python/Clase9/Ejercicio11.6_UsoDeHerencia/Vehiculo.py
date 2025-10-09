#Creamos la clase Padre, Vehiculo
class vehiculo:
    def __init__(self, color, ruedas ):#Establecemos los atributos de la clase padre
        self.color = color#Metodos de la clase padre
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo [Color = {self.color} - Ruedas = {self.ruedas}]'
    
