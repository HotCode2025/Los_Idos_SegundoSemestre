//Ejercicio 6: Pedir numeros hasta que se teclee 0 
//mostrar la suma de todos los numeros introducidos

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;
        int suma = 0;

        System.out.println("Ingrese numeros para sumar (0 para terminar):");

        while (true) {
            System.out.print("Numero: ");
            numero = sc.nextInt();

            if (numero == 0) {
                break; // Sale del ciclo si el número es 0
            }

            suma += numero; // Acumula la suma
        }

        System.out.println("La suma total es: " + suma);
        sc.close();
    }
}