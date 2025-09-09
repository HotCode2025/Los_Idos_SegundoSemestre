#Ejercicio2: Funcion con *args para multiplicar
#crear una funcion para multiplicar los valores recibidos
#de tipo numerico, utilizando argumentos variables *args
#como parametro de la función y regresar como resultado
#la multiplicación de todos los valores pasados como argumento

def multiplicar(*args):
    """Multiplica todos los valores numéricos recibidos."""
    resultado = 1
    for valor in args:
        if isinstance(valor, (int, float)):
            resultado *= valor
        else:
            raise ValueError(f"El valor '{valor}' no es numérico.")
    return resultado
