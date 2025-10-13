
package dominio;

public class Persona {
    //Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Persona (String nombre, double sueldo, boolean eliminado){
        this.nombre  = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    //Métodos

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {  //Para un atributo Boolean, no se usa "get", se utiliza "is" debido a que analiza si es True/False.
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    public String toSring(){  //El método toString convierte en cadena cada atributo
        return "Persona [nombre: "+this.nombre+
                ", sueldo:"+this.sueldo+
                ", eliminado"+this.eliminado+" ]"; 
    }
    
    public String toString(){  //El método toString convierte en cadena cada atributo
        return "Persona [nombre: "+this.nombre+
                ", sueldo: "+this.sueldo+
                ", eliminado: "+this.eliminado+ " ]";
    }
}
