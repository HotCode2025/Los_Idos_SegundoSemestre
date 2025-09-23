#Crear una clase llamada rectangulo, debe tener 2 atributos: Altura y base el nombre del método
#sera calcular area utilizando la formula:
#area = base * altura. Pero la base y la altura debe ser ingresados por el usuario y los objetos deben ser tres. 

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
rectangulos = []
for i in range(3):
    print(f"\nRectángulo {i+1}")
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    rect = Rectangulo(base,altura)
    rectangulos.append(rect)

for i, rect in enumerate(rectangulos, 1):
    print(f"El área del rectángulo {i}: {rect.calcular_area()}")
