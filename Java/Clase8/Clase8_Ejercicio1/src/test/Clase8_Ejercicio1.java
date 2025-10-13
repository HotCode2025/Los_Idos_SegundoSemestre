//Clase8_Java: Ejercicio: Crear otro objeto de tipo persona y asignar valores de manera inicial. Imprimir, modificar valores y volver a imprimir.
package test;

import dominio.Persona;
   
public class Clase8_Ejercicio1 {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 su nombre es = " + persona1.getNombre());
        //Modificar a través de los métodos:
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; => Ya no se puede utilizar (atributo privado)
        //System.out.println("Nombre es:" persona1.nombre); => Error
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 el resultado para obtener el booleano:  " + persona1.isEliminado());            
        
        //Tarea: Crear otro objeto de tipo persona y asignar valores de manera inicial. Imprimir, modificar valores y volver a imprimir.
        Persona persona2 = new Persona("Federico", 67000, true); //Creamos otro objeto de la clase Persona y pasamos argumentos para los atributos.
        System.out.println("nombre del objeto 2: " + persona2.getNombre());  //Llamamos al método get y mostramos cada atributo de manera separada.
        System.out.println("sueldo del objeto 2: " + persona2.getSueldo());
        System.out.println("booleano del objeto 2 = " + persona2.isEliminado());
        persona2.setNombre("Ramiro");       //Llamamos al método set y modificamos cada uno de los atributos.
        persona2.setSueldo(90000);
        persona2.setEliminado(false);
        System.out.println("nombre del objeto 2: " + persona2.getNombre());     //Volvemos a llamar al método get para cada atributo y mostramos su nuevo contenido.
        System.out.println("sueldo del objeto 2: " + persona2.getSueldo());
        System.out.println("booleano del objeto 2 = " + persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1);
        
        System.out.println("persona1: "+persona1.toString());  // No es necesaria la sintaxis .toString() sino que ya lo llama solo cuando imprimimos el objeto.
        System.out.println("persona1: "+persona1); // En esta línea el método toString se llama automáticamente como se mencionó arriba.
    }
}
