//Clase_11 Java: Arreglos

package test;


public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int[3]; //Lado izquierdo declaramos la variable. En el lado derehco instanciamos un objeto de tipo object.
        System.out.println("edades = " + edades);
        
        edades[0] = 17;  //Nota LOS ARREGLOS NO PUEDEN MODIFICARSE DE MANERA DINÁMICA (sí en Colecciones)
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 19;
        System.out.println("edades 1 = " + edades [1]);
        edades[2] = 21;
        System.out.println("edades 2 = " + edades [2]);
        
        // edades[3] = 7;  //Fuera de rango, error en tiempo de ejecución
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("Edades y sus elementos"+i+": "+edades[i]);
        }        
    }
}
