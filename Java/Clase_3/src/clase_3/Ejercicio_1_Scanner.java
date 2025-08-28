/*
Ejercicio 3: Leer números hasta que se instroduzca un cero.
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner y luego con la clase JOptionPane
 */
package clase_3;

import java.util.Scanner;

public class Ejercicio_1_Scanner {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int num;
 
        //Ciclo de mensajes hasta que sea cero
        do {
            System.out.print("Introduce un número ó cero (0) para salir: ");
            num = scanner.nextInt();
            
            if (num != 0) {
                if (num % 2 == 0) {
                    System.out.println(num + " es PAR");
                } else {
                    System.out.println(num + " es IMPAR");
                }
            }
            
        } while (num != 0);
        
    }
}
