class MiClase:

    #Variable de clase: este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase' #Se carga en memoria

    def __init__(self, variable_instancia): #La variable instancia da direfentes valores
        self.variable_instancia = variable_instancia
    

    @staticmethod #Modifica el metodo para asociarlo a la clase y no al objeto. El metodo estatico no puede acceder al dinamico ni a los atributos
    def metodo_estatico():#Desaparece el self, el metodo estatico no recibe la palabra self, por que self hace referencia al objeto
        print('-------Método estático-----------')
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls): #CLS: referencia a la clase en si mismo.
        print('--------Método de Clase----------')
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

print(MiClase.variable_clase)

MiClase1 = MiClase('Esta es una variable de instancia')
print(MiClase1.variable_instancia)
#Los objetos tambien puede acceder a una variable de clase, se puede acceder y ver el mismo resultado
print(MiClase1.variable_clase)

MiClase2=MiClase('Esta es otra prueba de la variable de instancia')
print(MiClase2.variable_instancia)#Si cambia cuando instanciamos
print(MiClase2.variable_clase)#No cambia cuando accedemos la a clase, muestra lo mismo


#Al crear una nueva clase hay que asignarle un valor
MiClase.variable_clase2 = 'Valor de variable clase 2'
print(MiClase.variable_clase2)
print(MiClase1.variable_clase2)#variable_clase2: No se ve disponible cuando escribimos el punto, porque no fue definida dentro del punto
print(MiClase2.variable_clase2)


#Existen dos tipos de metodos:
#-Estaticos: Se asocian a la clase, para ejercutarlo será a traves de la clase y luego llamamos al método estatico. Para indicar un metodo estatico se usa un decorador @staticmethod
#-De clase: Usamos un decorador @classmethod
MiClase.metodo_estatico()
MiClase.metodo_clase()

miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()