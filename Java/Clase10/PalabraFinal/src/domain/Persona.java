
package domain;

//public final class Persona => Esto evitaría que se creen clases child
public class Persona {
    public final static int CONSTANTE_AQUI = 15; // No se puede modificar
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
        
    //public final void imprimir() => Esto impediría modificar el método.
    public void imprimir(){
        System.out.println("Método para imprimir");
    }
}
