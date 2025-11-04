from Orden import orden
from Producto import Producto



producto1 = Producto('camiseta', 100.000)
producto2 = Producto('Pantalon', 150.000)
producto3 = Producto('Zapatos', 200.000)
producto4 = Producto('Gorra', 50.000)
producto5 = Producto('Campera', 250.000)
producto6 = Producto('Blusa', 75.000)

productos1 = [producto1, producto2] #Lista de productos
orden1 = orden(productos1)#Primero objeto pasando la lista de productos
#AGREGAMOS LOS PRODUCTOS 5 Y 3, a la orden 1:
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto3)
print(orden1)
print(F'TOTAL DE LA ORDEN 1: {orden1.calcular_total()}')

productos2 = [producto3, producto4]
orden2 = orden(productos2)
#AGREGAMOS LOS PRODUCTOS 6 Y 2, A LA ORDEN 2:
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(F'TOTAL DE LA ORDEN 2: {orden2.calcular_total()}')