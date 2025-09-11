//Ejercicio 9: Pedir el dia, mes y año de una fecha e
//indicar si la fecha es correcta. suponiendo que 
//todos los meses son de 30 dias
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Clase5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dia = 0, mes = 0, anio = 0;
        boolean fechaValida = false;

        while (!fechaValida) {
            try {
                dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día (1-30):"));
                mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes (1-12):"));
                anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año (>0):"));

                if (dia >= 1 && dia <= 30 && mes >= 1 && mes <= 12 && anio > 0) {
                    fechaValida = true;
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es válida: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "Fecha inválida. Intente nuevamente.");
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Entrada no válida. Por favor ingrese números enteros.");
            }
        }

  
    }
}