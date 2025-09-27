
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //Métodos
    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;  //Retornamos directamente la operacion (otra forma de escribirlo).
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a;  //La  variable "this" se crea atumáticamente durante la ejecución del método (señala el espacio de memoria que tiene la variable (a y b). "this" es un operador que señala a otros métodos/puntos.
        this.b = b; //al finalizar la ejecución. La varaible "this" se elimina. El argumento "a" se asigna al atributo "this.a". Uso Opcional por ahora, mejora legilibilidad. Hace que se diferencien el atributos de los argumentos (aunque tengan el mismo nombre)
        //return a + b; Podemos usar return para devolver directamente el resultado de la operación)
        return sumarConRetorno(); //O podemos llamar a otro método que ejecute la operación internamente y traiga el resultado. Los métodos tienen scope de clase.
    }    
}
