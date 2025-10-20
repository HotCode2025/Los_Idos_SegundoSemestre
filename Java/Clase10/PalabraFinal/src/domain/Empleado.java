
package domain;

public class Empleado extends Persona {
   @Override
    public void imprimir(){ //Si el método contuviera "final" esto no se puede hacer
       System.out.println("Método imprimir desde la clase hija");
   }
}
