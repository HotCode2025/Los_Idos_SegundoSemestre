from Producto import Producto

class orden:
    contador_ordenes = 0

    def __init__(self, productos):
        orden.contador_ordenes += 1
        self.id_orden = orden.contador_ordenes
        self._productos = list(productos)

#Agregamos un metodo para agregar un producto de manera independiente
    def agregar_producto(self, producto):
        self._productos.append(producto) #Esto es para agregar un nuevo producto


    def calcular_total(self):
        total = 0 #Variable temporal para almacenar total temporal.
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos: #Por cada producto vamos llamando a producto str
            productos_str += producto.__str__() + '|'#Por cada producto lo vamos almacenando y concatenando llamando al producto str
        return f'Orden: {self.id_orden}, \n Producto: {productos_str} '

if __name__ == '__main__':
    producto1 = Producto('camiseta', 100.000)
    print(producto1)
    producto2 = Producto('Pantalon', 150.000)
    print(producto2)

    productos1 = [producto1, producto2] #Lista de productos
    orden1 = orden(productos1)#Primero objeto pasando la lista de productos
    print(orden1)
    orden2 = orden(productos1)
    print(orden2)
