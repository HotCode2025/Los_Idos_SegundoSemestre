import random

# Se genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento < numero_secreto:
        print("Es mayor")
    elif intento > numero_secreto:
        print("Es menor")
    else:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
        break