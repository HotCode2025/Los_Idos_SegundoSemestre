//Clase6_Ejercicio3_JOptionPane:  Pedir un número y calcular su factorial.
// Hacerlo con las dos clases, Scanner y JOptionPane.

package Clase6_Ejercicio3;

import javax.swing.JOptionPane;

public class Clase6_Ejercicio3_JOptionPane {
        public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número para calcular su factorial:"));        
        long factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }        
        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }    
}
