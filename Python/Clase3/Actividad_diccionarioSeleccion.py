diccionarioDeCampeones = {
    10: {'Nombre':'Leonel Messi','Edad':38,'Altura':1.70,'Precio':'15 millones USD', 'Posicion':'Delantero / Mediocampista ofensivo'},
    9: {'Nombre':'Jualian Alvarez','Edad':25,'Altura':1.70,'Precio':'90 millones USD', 'Posicion':'Delantero centro'},
    8: {'Nombre':'Enzo Fernendez','Edad':24,'Altura':1.78,'Precio':'80 millones USD', 'Posicion':'Mediocampista central'},
    13: {'Nombre':'Cristian Romero','Edad':27,'Altura':1.85,'Precio':'65 millones USD', 'Posicion':'Defensor central'}
}

'''
print(diccionarioDeCampeones)

print(diccionarioDeCampeones[9])    #solo veo el 9, julian Alvarez

for num in diccionarioDeCampeones:    #solo veo los valores (num de la camiseta)
    print(num)

for valor in diccionarioDeCampeones.values():   #veo todos los datos ordenados sin valores
    print(valor)

    '''

for num, valor in diccionarioDeCampeones.items():   #Veo todo completo y ordenado
    print(num, valor)

print('La cantidad de elementos cargados son:', len(diccionarioDeCampeones))