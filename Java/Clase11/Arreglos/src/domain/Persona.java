//Clase_11 Java: Arreglos/Matrices

package domain;

public class Persona {
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;
    
    public Persona (){ //En este caso, esta clase tiene 3 constructores. Esto se llama SOBRECARGA de Constructores (2 o más).
    
    }
    public Persona (String nombre){
        this.nombre = nombre;
    }
     public Persona (String nombre , char genero, int edad , String direccion){
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }
     public String getDireccion(){
     return this.direccion;
     }
     public void setDireccion(String direccion){
     this.direccion = direccion;
     }
     public String getNombre(){
     return this.nombre;
     }
     public void setDirNombre(String nombre){
     this.nombre = nombre;
     }
      public char getGenero(){
     return this.genero;
     }
     public void setGenero(char genero){
     this.genero = genero;
     }
       public int getEdad(){
         return this.edad;
     }
     public void setEdad(int edad){
     this.edad = edad;
     }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}' + ", "+super.toString();
    }
     
}