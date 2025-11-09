import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)  #De manera indirecta llama al str de la clases Empleado o Gerente
    print(type(objeto))  #Esto es para saber que tipo de dato recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)



empleado = Empleado.Empleado('Ariel', 50000)
imprimir_detalles(empleado)

gerente = Gerente('Natalia', 60000, 'Sistemas')
imprimir_detalles(gerente)
