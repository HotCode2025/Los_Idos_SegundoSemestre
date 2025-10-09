from Vehiculo import vehiculo #Llamamos a la clase Vehiculo

class Auto(vehiculo):#Creamos la clase Auto a partir de la clase vehiculo(padre)
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)#VCS reconocio a Super por autocompletado
        self.velocidad = velocidad

    def __str__(self):
        return f'Auto [Color = {self.color} - Rueda = {self.ruedas} - Velocidad: {self.velocidad} Km/h]'
    