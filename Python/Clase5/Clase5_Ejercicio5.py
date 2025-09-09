# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funcions recursivas
# Puede ser cualquier valor positivo, por ej si se ingresa 5 debe imprimir:
# 5 4 3 2 1
# Si se ingresan numeros negativos no imprime nada


def imprimir_descendente(n):
    if n <= 0:
        return
    print(n, end=' ')
    imprimir_descendente(n - 1)

numero = int(input("Ingresa un número positivo: "))

if numero > 0:
    imprimir_descendente(numero)
else:
    print("El numero debe ser entero positivo.")
