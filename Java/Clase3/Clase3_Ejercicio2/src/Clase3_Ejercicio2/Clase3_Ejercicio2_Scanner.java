/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido. Lo hacemos primero con la clase Scanner y luego lo hacemos con la clase JOptionPane
 */
package Clase3_Ejercicio2;

import java.util.Scanner;

public class Clase3_Ejercicio2_Scanner {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num;
        int count = 0;
        System.out.println("Ingrese un número:");
        
        num = Integer.parseInt(entrada.nextLine());
        while (num >= 0){
            count++;
            System.out.println("Número ingresado: " + num);
            System.out.println("Números introducidos hasta ahora: " + count);
            System.out.println("Ingrese otro número:");
            num = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa terminó con un número negativo.");
        System.out.println("La cantidad de números que se introdujeron fue: " + count);
          
    }
    
}

