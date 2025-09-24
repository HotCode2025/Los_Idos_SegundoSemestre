/*Ejercicio 2 (11): Diseñar un programa que muestre el producto de los 10 primeros numeros impares. hacerlo con Scanner
 */

package clase6_ejercicio2_scanner;

import java.util.Scanner;

public class Clase6_Ejercicio2_Scanner {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        long producto = 1;
        String numeros = "";
        
        for (int i = 1, contador = 1; contador <= 10; i += 2, contador++) {
            producto *= i;
            numeros += i + (contador < 10 ? " × " : "");
        }
        
        System.out.println("Producto de: " + numeros + " = " + producto);
        scanner.close();
        
    }
    
}
