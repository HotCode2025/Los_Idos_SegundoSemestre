//Clase10_Java_Operaciones:

package operaciones;

public class Operaciones {
    public static int  sumar(int a, int b){
        System.out.println("Método para sumar enteros");
        return a+ b;
    }
    
    public static double sumar(double a, double b){ //NOTA IMP: Si el primer método es de tipo public, el siguiente no puede hacerse más restrictivo (private, protected, etc.)
        System.out.println("Método para sumar double");
        return a + b;
    }
}
