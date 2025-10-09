#iMPORTAMOS LA CLASE PADRE (VEHICULO) E HIJAS (AUTO - BICICLETA)
from Vehiculo import vehiculo
from Auto import Auto
from Bicicleta import Bicicleta


if __name__ == "__main__":
    vehiculo1 = vehiculo("Rojo" , 4)
    Auto1 = Auto("Negro", 4, 180)
    Bicicleta1 = Bicicleta("VerdeFluor", 2, "Montaña")

    print(vehiculo1)
    print(Auto1)
    print(Bicicleta1)

