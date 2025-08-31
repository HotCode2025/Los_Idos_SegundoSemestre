/*
Clase2_Ejercicio1_Scanner
Ejercicio: Leer un número y mostrar su cuadrado, repetir 
el proceso hasta que se introduzca un número negativo.
*/

package Clase2_Ejercicio1;

import javax.swing.JOptionPane;

public class Clase2_Ejercicio1_JOptionPane {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número del que desee conocer su cuadrado. "
                + "\nDigite un número negativo para finalizar el programa."));
            while (numero >= 0){                                                      
            var cuadrado = Math.pow(numero, 2); //Función que eleva el número al cuadrado Math.pow(base, exp)
            System.out.println("El cuadrado de "+numero+" es: "+cuadrado);
            numero =  Integer.parseInt(JOptionPane.showInputDialog("Digite otro número."));  //Solicitamos otro número y volvemos a evaluar la condición.
        }
        JOptionPane.showMessageDialog(null, "El programa finalizó al ingresar un número negativo."); //Mostramos mensaje de programa finalizado.          
    }
}
