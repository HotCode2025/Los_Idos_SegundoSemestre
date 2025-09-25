/*Ejercicio 1 (10): Pedir 10 números y escribir la suma total. Hacerlo con la clase JOptionPane
 */

package clase6_ejercicio1_joptionpane;

import javax.swing.JOptionPane;

public class Clase6_Ejercicio1_JOptionPane {


    public static void main(String[] args) {

       int suma = 0;
        
       JOptionPane.showMessageDialog(null, "Ingrese 10 números:");
        
       for (int i = 1; i <= 10; i++) {
            String input = JOptionPane.showInputDialog("Número " + i + ":");
            int numero = Integer.parseInt(input);
            suma += numero;
       }
        
       JOptionPane.showMessageDialog(null, "La suma total es: " + suma);
        
    }
    
}
