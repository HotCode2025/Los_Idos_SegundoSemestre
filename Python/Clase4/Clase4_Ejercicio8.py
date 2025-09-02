#Ejercicio 8: Factorial de un numero positivo
#Hacer un programa para calcular el factorial de un numero positivo

while True: #Comprueba que se seleccione correctamente el numero, simula un ciclo do-while

    num = int(input('Ingresa el numero positivo para calcular su factorial:'))
  
    if num >= 0:
        break   #corta el ciclo al cumplirse la condicion
    else:
        print('Error: ingrese un numero POSITIVO')
    

if num == 0 or num == 1:
    fact = 1
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i


#Forma de hacerlo con math.factorial(mucho mas simple)

#    import math

#   fact = math.factorial(num)


print(f'El factorial de {num} es {fact}')


