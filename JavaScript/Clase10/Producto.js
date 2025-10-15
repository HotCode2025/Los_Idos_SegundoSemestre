class Producto{
    static contadorProductos = 0;
   
    //Constructor
    constructor(nombre, precio){
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    //Métodos
     get IdProducto(){
        return this._idProducto;
     }

     get Nombre(){
        return this._nombre;
     }

     set Nombre(nombre){
        this._nombre = nombre;
     }

     get Precio(){
        return this._precio;
     }

     set Precio(precio){
        if (precio < 0) throw new Error('El precio no puede ser negativo');
        this._precio = precio;
     }

    toString() {
        return `ID: ${this._idProducto}, Nombre: ${this._nombre}, Precio: $${this._precio}`;
    }

}