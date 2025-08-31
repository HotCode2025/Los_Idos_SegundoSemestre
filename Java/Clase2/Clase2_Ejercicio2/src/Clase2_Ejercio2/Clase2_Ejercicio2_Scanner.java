/*
Clase2_Ejercicio2_Scanner
Ejercicio: Leer un número e indicar si es positivo o negativo.
El proceso se repetirá hasta que se introduzca un cero 0.
*/
package Clase2_Ejercio2;

import java.util.Scanner;

public class Clase2_Ejercicio2_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); //Creamos una entrada tipo Scanner.
        System.out.println("Ingrese un número. \nDigite cero para finalizar el programa");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0){
            if (numero > 0){
                System.out.println("El número es positivo.");
            }else{
                System.out.println("El número es negativo.");
            }
            System.out.println("Por favor ingrese otro número.");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa ha finalizado al ingresar 0.");
    }
}
