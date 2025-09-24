//Clase6_Ejercicio3_Scanner:  Pedir un número y calcular su factorial.
// Hacerlo con las dos clases, Scanner y JOptionPane.

package Clase6_Ejercicio3;

import java.util.Scanner;

public class Clase6_Ejercicio3_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);        
        System.out.print("Digite un número para calcular su factorial: ");
        int numero = entrada.nextInt();        
        long factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }        
        System.out.println("El factorial de " + numero + " es: " + factorial);
    }
}


