//Clase10_Java_Palabra final

/*
Uso de la palabra Final:
- 
Esta palabra tiene diferentes significados dependiendo dónde se aplique
    - Variables: Evita cambiar el valor que almacena la variable.
    - Métodos: Evita que se modifique la definición o el comportamiento de un método
               de una subclase(hija)
    - Clases: Evita que se creen clases hijas

Otra característica es que normalmente, cuando trabajamos con variables, 
se combina con el modificador de acceso estático para convertir una variable
en una constante, es decir que no se puede modificar su valor. El ejemplo
de esto es la clase Math, en la cual todos sus atributos son de tipo static y final,
es por esto que la variable pi* se conoce como una constante.
*/

package test;
import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 36632645;
        System.out.println("miDni = " + miDni);
        //miDni = 20312662; No se puede modificar porque la variable se declaró con "final"
        //Persona.CONSTANTE_AQUI = 9; => NO se modifica porque se declaró como final const.        
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
    final Persona persona1 = new Persona();
    //persona1 = new Persona(); => No se puede asignar una nueva referencia (final)
    persona1.setNombre("Nicolas Giglio");
    System.out.println("persona1 nombre: "+persona1.getNombre());
    persona1.setNombre("Liliana"); 
    System.out.println("persona1 nombre: "+persona1.getNombre());
    }
}
