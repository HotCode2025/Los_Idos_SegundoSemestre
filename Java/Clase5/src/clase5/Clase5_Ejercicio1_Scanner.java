/*Ejercicio 1: Pedir un numero N y mostrar todos los numeros del 1 al N - Scanner
 */

package clase5;

import java.util.Scanner;

public class Clase5_Ejercicio1_Scanner {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese un numero:");
        int num = scanner.nextInt();
        
        System.out.println("Lista de números del 1 al " + num + " :");
        
        for (int i = 1; i <= num; i++)  {
            System.out.print(i + " ");
        }
        
        scanner.close();
        
    }
    
}
