class Producto:
    contador_productos = 0 #Variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #Aumento para la variable de clase
        self._id_producto = Producto.contador_productos #Asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio

#Metodos getter and setter
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio


#Sobreescribimos el metodo srt
    def __str__(self):
        return f'id Producto: {self._id_producto}, nombre: {self.nombre}, precio: {self.precio}'
    
if __name__ == ' __main__ ': #Solo será visible si la prueba se ejecuta desde acá
    producto1 = Producto('camiseta', 100.000)
    producto2 = Producto ('Pantalon', 150.000)