//Clase_11 Java: Matrices

package test;

import domain.Persona;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int [3][2];
        System.out.println("edades = " + edades);
        
        edades[0][0] = 5; //Llenado manual de la matriz
        edades[0][1] = 7; //Es una columna diferente
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 6;
        edades[2][1] = 3;
        
        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 2-0 = " + edades[2][0]);
        System.out.println("edades 2-1 = " + edades[2][1]);
        
        for(int fila = 0; fila < edades.length; fila++){
            for (int col = 0; col < edades[fila].length; col++) {
                   System.out.println("edades "+fila+"-"+col+": "+edades [fila][col]);
            }
        } 
        // Sintaxis clásica.
        //String frutas[][] = new String[3][2];
        
        //Sintaxis simplificada:
        String frutas[][] = {{"Límón", "Pomelo"},{"Ciruela","Kiwi"},{"Banana", "Manzana"}};      
        
        //Llamamos al método imprimir declarado fuera del main:
        imprimir(frutas);
        
//         for(int i = 0; i < frutas.length; i++){
//            for (int j = 0; j < frutas[i].length; j++) {
//                   System.out.println("frutas "+i+"-"+j+": "+frutas [i][j]);
//            }
//        }
         //Creamos una matriz de objetos (de la clase Persona)
        Persona personas[][] = new Persona[2][3];
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Nicolas");
        personas[0][1] = new Persona("Ramón");
        personas[0][2] = new Persona("Pepe");
        personas[1][0] = new Persona("Luis");
        personas[1][1] = new Persona("Ana");
        personas[1][2] = new Persona("Rodrigo");
        
        imprimir(personas);
    }
    
    //Creamos un método fuera del main => Se llama en la lín 38 reemplazando el for (cumple la misma función)
    public static void imprimir(Object matriz[][]){  //Este método 
         for(int i = 0; i < matriz.length; i++){
            for (int j = 0; j < matriz[i].length; j++) {
                   System.out.println("matriz"+i+"-"+j+": "+matriz [i][j]);
            }
        }       
    }    
}
