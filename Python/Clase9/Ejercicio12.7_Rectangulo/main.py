from rectangulo import Rectangulo
from cuadrado import Cuadrado

if __name__ == "__main__":
    rectangulo1 = Rectangulo(5, 3, "rojo")
    print(rectangulo1)

    cuadrado1 = Cuadrado(4, "azul")
    print(cuadrado1)

    
    cuadrado1.color = "verde"
    cuadrado1.ancho = 6  
    print(cuadrado1)
