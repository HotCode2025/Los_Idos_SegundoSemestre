/*Ejercicio 1: Pedir un numero N y mostrar todos los numeros del 1 al N - JOptionPane
 */

package clase5;

import javax.swing.JOptionPane;

public class Clase5_Ejercicio1_JOptionPane {

    public static void main(String[] args) {
        
        String input = JOptionPane.showInputDialog("Ingrese un número: ");     
        int num = Integer.parseInt(input);
        
        /* String numeros = "";
        
        for (int i = 1; i <= num; i++)  {
            numeros = numeros + i + " ";
        }*/      
                
       StringBuilder numeros = new StringBuilder(); // Opcion adecuada cuando es, o puede ser, una concatenacion larga
        
        for (int i = 1; i <= num; i++)  {
            numeros.append(i).append(" ");
        }
                
        JOptionPane.showMessageDialog(null, "Lista de números del 1 al " + num + ":\n" + numeros);
                
    }
    
}