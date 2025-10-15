class Orden{
    static contadorOrdenes = 0;
    static MAX_PRODUCTOS = 5;

    //Constructor
    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    //Métodos
    agregarProducto(producto) {
        if (this._contadorProductosAgregados < Orden.MAX_PRODUCTOS) {
            this._productos.push(producto);
            this._contadorProductosAgregados++;
            console.log('Producto agregado');
        } else {
            console.log('Su carrito ya está lleno (máximo de productos = 5)');
        }
    }   

    calcularTotal() {
        let total = 0;
        for (const p of this._productos) {
        total += p.getPrecio();
        }
        return total;
    }

    mostrarOrden(){

        console.log("Orden N°: " + this._idOrden);
        
        if (this._productos.length === 0) {
            console.log("No hay productos en la orden.");
        } else {
            console.log("Productos:");
        for (let i = 0; i < this._productos.length; i++) {
            let producto = this._productos[i];
            console.log((i + 1) + ". " + producto.nombre + " - $" + producto.precio);
            }
            console.log("Total: $" + this.calcularTotal());
        }
    }

}