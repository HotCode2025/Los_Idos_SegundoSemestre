/*Clase_3_Java_Ejercicio_1: Clase Scanner
Ejercicio: Leer números hasta que se introduzca un cero.
Para cada uno indicar si es par o impar.
*/
package Clase3_Ejercicio3;

import java.util.Scanner;

public class Clase3_Ejercicio3_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero_aleatorio, numero, intentos = 0;
        numero_aleatorio = (int) (Math.random()* 100);
        System.out.println(numero_aleatorio);
        System.out.println("Digite un número para adivinar si acierta: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero != numero_aleatorio){
         intentos++;
         if (numero > numero_aleatorio){
             System.out.println("El número ingresado es mayor al esperado");
         }else{
             System.out.println("El número ingresado es menor al esperado");
         }
          System.out.println("Ingrese otro número");
          numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Usted ha adivinado! El número secreto es: "+numero_aleatorio+" y le ha requerido "+intentos+" intentos!");
        System.out.println("Felicitationes!");
    }    
}
