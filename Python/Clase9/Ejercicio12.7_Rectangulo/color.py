class Color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._color = valor
        else:
            raise ValueError("El color debe ser una cadena no vacía.")

    def __str__(self):
        return f"Color[color={self._color}]"
