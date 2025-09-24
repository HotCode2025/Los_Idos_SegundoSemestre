/*Ejercicio 2 (11): Diseñar un programa que muestre el producto de los 10 primeros numeros impares. hacerlo con JOptionPane
 */
package clase6_ejercicio2_joptionpane;

import javax.swing.JOptionPane;

public class Clase6_Ejercicio2_JOptionPane {

    public static void main(String[] args) {

        long producto = 1;
        String numeros = "";
        
        for (int i = 1, contador = 1; contador <= 10; i += 2, contador++) {
            producto *= i;
            numeros += i + (contador < 10 ? " × " : "");
        }
        
        JOptionPane.showMessageDialog(null, 
            "Producto de: " + numeros + " = " + producto, 
            "Resultado", 
            JOptionPane.INFORMATION_MESSAGE);
    }
    
}
