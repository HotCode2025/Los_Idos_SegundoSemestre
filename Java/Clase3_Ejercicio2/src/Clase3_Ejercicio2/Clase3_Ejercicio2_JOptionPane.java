/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido. Lo hacemos primero con la clase Scanner y luego lo hacemos con la clase JOptionPane
 */
package Clase3_Ejercicio2;

import javax.swing.JOptionPane;

public class Clase3_Ejercicio2_JOptionPane {
    
    public static void main(String[] args) {
        int num;
        int count = 0;
        
        String entrada = JOptionPane.showInputDialog("Ingrese un número: ");
        num = Integer.parseInt(entrada);
        
        while (num >= 0){
            count++;
            JOptionPane.showMessageDialog(null, "Número ingresado: " + num + "\nNúmeros introducidos hasta ahora: " + count );
            
            entrada = JOptionPane.showInputDialog("Ingrese otro número: ");
            num = Integer.parseInt(entrada);
                    
        }
        
        JOptionPane.showMessageDialog(null, "El programa terminó con un número negativo." + "\nTotal de números introducidos: " + count);
        
        }
    
}
