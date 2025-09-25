#Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un método calcular_volumen que tendrá la fórmula: volumen = ancho * altura * prfundidad que el usuario ingrese los valores

class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad
    
    @classmethod
    def datos(cls):
        ancho = float(input("Ingrese el ancho: "))
        altura = float(input("Ingrese la altura: "))
        profundidad = float(input("Ingrese la profundidad: "))
        return cls(ancho, altura, profundidad)

cubo1 = Cubo.datos()

print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')