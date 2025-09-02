# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma
# frase pero sin espacios en blanco y un contador de los caracteres que tiene
# la frese (sin contar los espacios en blanco)


frase_original = input("Ingresa una frase: ")

frase_sin_espacios = frase_original.replace(" ", "") # quita espacios de la frase

contador_caracteres = len(frase_sin_espacios) # cuenta caracteres sin espacios

print(f"La frase sin espacios es: '{frase_sin_espacios}'")
print(f"El número total de caracteres sin espacios es: {contador_caracteres}")