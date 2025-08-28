/*
Ejercicio 3: Leer números hasta que se instroduzca un cero.
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner y luego con la clase JOptionPane
 */

package clase_3;

   import javax.swing.JOptionPane;

public class Ejercicio_1_JOptionPane { 
 

    @SuppressWarnings("empty-statement")
    public static void main(String[] args) {
        
        int num;
        
        //Ciclo de mensajes hasta que sea cero
        do {
            String input = JOptionPane.showInputDialog(null,
                "Introduce un número ó cero (0) para salir: ",
                JOptionPane.QUESTION_MESSAGE);
            
            // Funcion de boton cancelar
            if (input == null) {
                break;
            }           
                num = Integer.parseInt(input);
                
                if (num != 0) {
                    String msj;
                    if (num % 2 == 0) {
                        msj = num + " es PAR";
                    } else {
                        msj = num + " es IMPAR";
                    }
                    
                    JOptionPane.showMessageDialog(null,
                        msj,
                        "El numero introducido",
                        JOptionPane.INFORMATION_MESSAGE);
                }            
        } while (num != 0);
    }
}


