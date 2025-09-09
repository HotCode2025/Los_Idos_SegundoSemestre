#Convertidor de temperatura. Realiza dos funciones para convertir de grados celsius a fahrenheit y viseversa.
#Investiga las fórmulas

#FÓRMULAS:
#Celsius a Fahrenheit: °F = (°C × 9/5) + 32
#Fahrenheit a Celsius: °C = (°F - 32) / 1.8

#Creamos la funciones para convertir la temperatura
def celsius_a_fahrenheit(celsius):
#Convertimos la temperatura de Celsius a Fahrenheit
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
#Convertimos la temperatura de Fahrenheit a Celsius
    return (fahrenheit - 32) * 5/9

# Ingresamos la temperatura que deseamos convertir
opcion = input("Desea convertir a (C)elsius o (F)ahrenheit? ").upper()
temp = float(input("Ingresa la temperatura: "))


if opcion == "F":
    resultado = celsius_a_fahrenheit(temp)
    print(f"{temp}°C = {resultado}°F")
elif opcion == "C":
    resultado = fahrenheit_a_celsius(temp)
    print(f"{temp}°F = {resultado}°C")
else:
    print("Opción no válida")
