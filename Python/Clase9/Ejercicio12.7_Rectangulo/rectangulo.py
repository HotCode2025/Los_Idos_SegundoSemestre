from figura_geometrica import FiguraGeometrica
from color import Color
#creamos cuadrado desde figura geometrica y color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            raise ValueError("El ancho debe ser mayor que cero.")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            raise ValueError("El alto debe ser mayor que cero.")

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return (
            f"Rectangulo[ancho={self.ancho}, alto={self.alto}, "
            f"color={self.color}, area={self.area()}]"
        )
