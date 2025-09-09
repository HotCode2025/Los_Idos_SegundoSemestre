# Ejercicio 3: Crear una funcion para sumar los valores recibidos de tipo numéricos, utilizando argumentos variables *args como parámetros de la funcion 
# y agregar como reusltado la suma de todos los valores pasados como argunmentos

def sumaValores(*args):
    return sum(args)

valores = []

print('Ingrese los valores a sumar (valor nulo finaliza la funcion)')

while True:
    entrada = input()
    if entrada == "":
        break
    else:
        num = float(entrada)
        valores.append(num)



print(f'Los valores ingresados son {valores}')
print(f'La suma de esos valores es {sumaValores(*valores)}')