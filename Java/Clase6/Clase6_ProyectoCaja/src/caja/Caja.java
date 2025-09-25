public class Caja {
    private double ancho;
    private double alto;
    private double profundidad;

    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public double getVolumen() {
        return ancho * alto * profundidad;
    }

    // getters y setters opcionales
}