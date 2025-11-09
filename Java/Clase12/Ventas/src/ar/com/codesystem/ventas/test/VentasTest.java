
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args){
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        //Agrego mas objetos de tipo Producto segun lo pedido en la TAREA
        Producto producto3 = new Producto("Remera", 8900.00);
        Producto producto4 = new Producto("Boxer", 3900.00);
        Producto producto5 = new Producto("Medias", 1900.00);
        Producto producto6 = new Producto("Gorra", 5000.00);
        Producto producto7 = new Producto("Camisa", 15000.00);
        
        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        //Agrego más objetos de tipo Orden según lo pedido en la TAREA
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto4);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto2);
        orden3.agregarProducto(producto3);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto4);
        orden3.agregarProducto(producto5);
        orden3.mostrarOrden();
        
        Orden orden4 = new Orden();
        orden4.agregarProducto(producto1);
        orden4.agregarProducto(producto5);
        orden4.agregarProducto(producto7);
        orden4.mostrarOrden();
        
        
        
        //Tarea: REALIZADA Y COMENTADA ARRIBA
        //Crear mas objetos de tipo Producto
        //Crear mas objetos de tipo Orden
        
    }
}
