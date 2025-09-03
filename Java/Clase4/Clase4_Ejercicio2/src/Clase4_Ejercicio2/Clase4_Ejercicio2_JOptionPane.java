//Clase4_Ejercicio2_Java:
/*
Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos.
*/

package Clase4_Ejercicio2;

import javax.swing.JOptionPane;

public class Clase4_Ejercicio2_JOptionPane {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número. Presione 0 para finalizar el programa"));
        int suma = 0;
        while (numero != 0){
            suma += numero;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número. Presione 0 para finalizar el programa"));
        }
        JOptionPane.showMessageDialog(null, "La sumatoria de todos los números ingresados es: " + suma);
        JOptionPane.showMessageDialog(null, "El Programa ha finalizado al ingresar 0");
    }
}
