# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde en una lista
# su tabla de multiplicar hasta el 10. Por ejemplo: si digita el 5
# la lista tendra: 5, 10, 15, 20, 25, 30, 35, 40, 45,50.

numero = int(input("Ingresa un número: "))

tabla_multiplicar = []

for i in range(1, 11):
    resultado = numero * i
    tabla_multiplicar.append(resultado)

print(f"La tabla de multiplicar del {numero} es: {tabla_multiplicar}")