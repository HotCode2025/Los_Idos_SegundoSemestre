# Crear una lista vacía para almacenar los personajes
personajes = []

# Agregamos el primer personaje
aragorn = {
    "Nombre": "Aragorn",
    "Clase": "Guerrero", 
    "Raza": "Dúnadan del norte"
}
personajes.append(aragorn)

# Agregamos el segundo personaje
gandalf = {
    "Nombre": "Gandalf",
    "Clase": "Mago",
    "Raza": "Maiar"
}
personajes.append(gandalf)

# Agregamos el tercer personaje
legolas = {
    "Nombre": "Legolas",
    "Clase": "Arquero",
    "Raza": "Elfo Sindar"
}
personajes.append(legolas)

# Mostramos la lista de personajes del señor de los anillos
print("Lista de personajes de El Señor de los Anillos:")
print("--------------------------------------------------")

for personaje in personajes:
    print(f"Nombre: {personaje['Nombre']}")
    print(f"Clase: {personaje['Clase']}")
    print(f"Raza: {personaje['Raza']}")
    print("------------------------------")