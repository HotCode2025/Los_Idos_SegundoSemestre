
package Operaciones;

public class PruebaArimetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica(); //Llamamos a constructor para crear una instancia de la clase Aritmetica (objeto)
        aritmetica1.a = 3; //Llamamos y pasamos valores para los atributos.
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros(); //Llamamos al método del objeto.
        
        int resultado = aritmetica1.sumarConRetorno(); //Llamamos a otro método del objeto.
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+ resultado);
    }
}