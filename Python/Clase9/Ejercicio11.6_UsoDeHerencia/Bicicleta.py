from Vehiculo import vehiculo

class Bicicleta(vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)#VCS reconocio a Super por autocompletado, traemos de la clase padre los atributos
        self.tipo = tipo

    
    def __str__(self):
        return f'Bicicleta [Color = {self.color} - Ruedas = {self.ruedas} - Tipo = {self.tipo}]'
    

