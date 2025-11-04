'''
SOBRECARGA DE OPERADORES:
Básicamente, la sobrecarga de un operador significa que un mismo operador puede comportarse de diferentes formas.
Por ejemplo, el operador de suma (+)
El operador de suma es un buen ejemplo de la sobrecarga de operadores.
Este operador se puede comportar de aneras distintas dependiendo si está trabajando con tipos string,
con tipos enteros o por ejemplo con tipos lista.
Así que dependiendo del tipo con el que esté trabajando, es el tipo de resultado que vamos a obtener.
Por lo tanto, un mismo operador puede trabajar de distintas formas..

'''

a = 3
b = 5
print(a+b) #Suma

a = 'hola'
b = 'mundo'
print(a+b) #Une

a = [1,2,3,4]
b = [5,6,7,8]
print(a+b) #concatena

#Sobrecarga con CLASES en python: 
'''
# Operadores Aritméticos	magic method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)

#Operadores Lógicos
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)

EL METODO QUE NECESITEMOS LO TENEMOS QUE SOBREESCRIBIR
'''
#Ahora, la sobrecarga y la sobreescritura son dos conceptos diferentes.
'''Recordemos que la sobrecarga de un operador
significa que se puede comportar de maneras
distintas dependiendo de los operandos con
los cuales esté trabajando y la sobreescritura
tiene que ver con herencia.'''

#miObjeto1 + miObejeto2 = Esto no se puede hacer, el operador necesita una sobrecarga para poder realizar la operacion


