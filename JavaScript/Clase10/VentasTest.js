// ===== Clase Producto =====
class Producto {
    static contadorProductos = 0;

    constructor(nombre, precio) {
        this._idProducto = ++Producto.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get IdProducto() {
        return this._idProducto;
    }

    get Nombre() {
        return this._nombre;
    }

    set Nombre(nombre) {
        this._nombre = nombre;
    }

    get Precio() {
        return this._precio;
    }

    set Precio(precio) {
        if (precio < 0) throw new Error('El precio no puede ser negativo');
        this._precio = precio;
    }

    toString() {
        return `ID: ${this._idProducto}, Nombre: ${this._nombre}, Precio: $${this._precio}`;
    }
}

// ===== Clase Orden =====
class Orden {
    static contadorOrdenes = 0;
    static MAX_PRODUCTOS = 5;

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    get idOrden() {
        return this._idOrden;
    }

    agregarProducto(producto) {
        if (!(producto && typeof producto.Precio === 'number')) {
            console.log('El objeto agregado no es un producto válido.');
            return;
        }

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
        for (let i = 0; i < this._productos.length; i++) {
            total += this._productos[i].Precio;
        }
        return total;
    }

    mostrarOrden() {
        console.log("Orden N°: " + this._idOrden);

        if (this._productos.length === 0) {
            console.log("No hay productos en la orden.");
        } else {
            console.log("Productos:");
            for (let i = 0; i < this._productos.length; i++) {
                let producto = this._productos[i];
                console.log((i + 1) + ". " + producto.Nombre + " - $" + producto.Precio);
            }
            console.log("Total: $" + this.calcularTotal());
        }
    }
}

// ===== Clase de prueba VentasTest =====
console.log("=== PRUEBA DE VENTAS ===");

let producto1 = new Producto("Vino Malbec", 12000);
let producto2 = new Producto("Espumante Brut", 15000);
let producto3 = new Producto("Vino Cabernet", 10000);
let producto4 = new Producto("Vino Chardonnay", 9000);
let producto5 = new Producto("Vino Merlot", 10000);
//let producto6 = new Producto("Vino Syrah", 13000);

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto4);
orden1.agregarProducto(producto5);
//orden1.agregarProducto(producto6);


orden1.mostrarOrden();
