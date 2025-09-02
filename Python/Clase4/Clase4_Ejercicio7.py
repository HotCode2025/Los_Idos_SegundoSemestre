#Ejercicio 7: Sumar numeros pares dentro de un rango
#Hacer un programa que sume numeros pares dentro de un rango por ejemplo:
#suma de numeros pares del 2 al 20
#suma = 240

print('Ingresa un rango de numeros para realizar la suma de los numeros pares')

suma = 0

while True: #Comprueba que se seleccione correctamente el rango, simula un ciclo do-while

    numIn = int(input('ingresa el numero mas bajo del rango'))
    numOut = int(input('ingresa el numero mas alto del rango'))

    if numIn <= numOut:
        break   #corta el ciclo al cumplirse la condicion
    else:
        print('Error al ingresar el rango de numeros, intente nuevamente')
    

for num in range(numIn, numOut + 1):
    print(num)
    if num % 2 == 0:
        suma += num

print(f'La suma de todos los numeros pares en el rango del {numIn} al {numOut} es {suma}')

