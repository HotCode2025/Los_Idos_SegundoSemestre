import java.util.Scanner;

public class PruebaCaja {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ancho: ");
        double ancho = sc.nextDouble();
        System.out.print("Alto: ");
        double alto = sc.nextDouble();
        System.out.print("Profundidad: ");
        double profundidad = sc.nextDouble();
        sc.close();

        Caja caja = new Caja(ancho, alto, profundidad);
        System.out.printf("Volumen = %.4f%n", caja.getVolumen());
    }
}