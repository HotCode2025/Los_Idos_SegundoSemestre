/*Ejercicio 1 (10): Pedir 10 números y escribir la suma total. Hacerlo con la clase Scanner
 */

package clase6_ejercicio1_scanner;

import java.util.Scanner;

public class Clase6_Ejercicio1_Scanner {

    public static void main(String[] args) {

                Scanner scanner = new Scanner(System.in);
        int suma = 0;
        
        System.out.println("Ingrese 10 números:");
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("Número " + i + ": ");
            int numero = scanner.nextInt();
            suma += numero;
        }
        
        System.out.println("La suma total es: " + suma);
        scanner.close();

    }
    
}
