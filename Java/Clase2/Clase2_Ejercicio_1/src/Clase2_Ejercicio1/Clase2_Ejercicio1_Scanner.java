/*
Clase2_Ejercicio1_Scanner
Ejercicio: Leer un número y mostrar su cuadrado, repetir 
el proceso hasta que se introduzca un número negativo.
*/

package Clase2_Ejercicio1;

import java.util.Scanner;

public class Clase2_Ejercicio1_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); //Creamos una entrada tipo Scanner.
        System.out.println("Digite un número del que desee conocer su cuadrado. "
                + "Digite un número negativo para finalizar el programa.");
        var numero = Integer.parseInt(entrada.nextLine()); //Asignamos a la variable "numero" lo ingresado por el Usuario.
        while (numero >= 0){                                                      
            var cuadrado = Math.pow(numero, 2); //Función que eleva el número al cuadrado Math.pow(base, exp)
            System.out.println("El cuadrado de "+numero+" es: "+cuadrado);
            System.out.println("Por favor ingrese otro número:");
            numero = Integer.parseInt(entrada.nextLine()); //Solicitamos otro número y volvemos a evaluar la condición.
        }
        System.out.println("Programa finalizado al ingresar número negativo"); //Si la condición no se cumple finaliza el programa
    }
}
