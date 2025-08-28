/*Clase_3_Java_Ejercicio_3: Clase Scanner
Ejercicio: Realizar un juego para adivinar un número, para ello generar un número aleatorio 
entre 0-100 y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor
o menor respecto a N.
El proceso termina cuando el usuario acierta y mostramos el número de intentos hechos.
*/
package Clase3_Ejercicio3;

import javax.swing.JOptionPane;

public class Clase3_Ejercicio3_JOptionPane {
    public static void main(String[] args) {
                int numero_aleatorio, numero, intentos = 0;
        numero_aleatorio = (int) (Math.random()* 100);
        System.out.println(numero_aleatorio);
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número para adivinar si acierta:"));
        while (numero != numero_aleatorio){
         intentos++;
         if (numero > numero_aleatorio){
             System.out.println("El número ingresado es mayor al esperado");
         }else{
             System.out.println("El número ingresado es menor al esperado");
         }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número para adivinar si acierta:"));
        }
        System.out.println("Usted ha adivinado! El número secreto es: "+numero_aleatorio+" y le ha requerido "+intentos+" intentos!");
        System.out.println("Felicitationes!"); 
    }    
}
