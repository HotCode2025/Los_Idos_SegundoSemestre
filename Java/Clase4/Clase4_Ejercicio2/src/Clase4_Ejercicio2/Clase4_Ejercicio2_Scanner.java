//Clase4_Ejercicio2_Java:
/*
Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos.
*/
package Clase4_Ejercicio2;

import java.util.Scanner;

public class Clase4_Ejercicio2_Scanner {
    public static void main(String[] args) {
            Scanner entrada = new Scanner(System.in);
            System.out.println("Por favor ingrese un número. Presione 0 para finalizar: ");  
            var numero = Integer.parseInt(entrada.nextLine());
            var suma = 0;
            while (numero != 0){
                suma += numero;
               System.out.println("Por favor ingrese otro número. Presione 0 para finalizar: ");  
            numero = Integer.parseInt(entrada.nextLine());             
            }
            System.out.println("La sumatoria de todos los números ingresados es: " + suma);
            System.out.println("El programa ha finalizado por ingreso de caracter 0");
    }
}
