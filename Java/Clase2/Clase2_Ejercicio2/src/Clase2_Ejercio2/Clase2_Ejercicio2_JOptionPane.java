/*
Clase2_Ejercicio2_JOptionPane
Ejercicio: Leer un número e indicar si es positivo o negativo.
El proceso se repetirá hasta que se introduzca un cero 0.
*/
package Clase2_Ejercio2;

import javax.swing.JOptionPane;

public class Clase2_Ejercicio2_JOptionPane {
    public static void main(String[] args) {
         var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite distinto de cero para saber si es negativo o positivo. "
                + "\nDigite un 0 para finalizar el programa.")); //Solicitamos el input con un mensaje.
         while (numero != 0){
            if (numero > 0){
                JOptionPane.showMessageDialog(null, "El número ingresado es positivo."); //Mostramos mensaje si se cumple la condicion.
            }else{
                 JOptionPane.showMessageDialog(null, "El número ingresado es negativo.");
            }
             numero = Integer.parseInt(JOptionPane.showInputDialog("Por favor ingrese otro número")); //Solicitamos otro número.   
        }
        JOptionPane.showMessageDialog(null, "El programa ha finalizado al ingresar 0"); //Mensaje de programa finalizado.
    }    
}
