
package Clase1_Ciclos;


public class Clase1_Ciclos {
 
    /*Ciclo While: Mientras*/
    
    public static void main (String[] args){
        System.out.println("Ciclo While");
        var conteo = 0;// Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;//Vamos aumentando en uno la variable
        }
        System.out.println("\nCiclo Do While");
        /*Ciclo Do While: Se ejecuta de forma diferente al while, primero el Do
        y despúes las lineas de codigo. */
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
        
        
        
        //Uso de las palabras break y continue junto a las etiquetas(labels)
        System.out.println("Palabra break, continue con labels");
        inicio:
        for(var contando = 0;contando < 7;contando++){
            if (contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;//Imprime solamente uno
            }
        }
        
        System.out.println("\nCiclo For, números pares Continue");
        /*Ciclo For*/
        inicio:
        for(var contando = 0;contando < 7;contando++){
            if (contando % 2 != 0){
               continue inicio;//vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }    
        
       
    }
}
 
    

