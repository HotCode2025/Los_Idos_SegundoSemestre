from figura_geometrica import FiguraGeometrica
from color import Color
#creamos cuadrado desde figura geometrica y color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    @FiguraGeometrica.ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
            self._alto = valor
        else:
            raise ValueError("El lado del cuadrado debe ser mayor que cero.")

    @FiguraGeometrica.alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
            self._ancho = valor
        else:
            raise ValueError("El lado del cuadrado debe ser mayor que cero.")

    def area(self):
        return self.ancho ** 2

    def __str__(self):
        return (
            f"Cuadrado[lado={self.ancho}, color={self.color}, area={self.area()}]"
        )
