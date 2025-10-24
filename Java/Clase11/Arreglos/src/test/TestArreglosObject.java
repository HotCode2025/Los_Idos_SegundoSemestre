//Clase_11 Java: Arreglos
package test;

import domain.Persona;

public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona [2];
        personas[0] = new Persona("Nicolas");
        personas[1] = new Persona("Robert");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = "+ personas[1]);     
        
        for(int i = 0; i < personas.length; i++){
            System.out.println("persona "+i+" = "+ personas[i]);
        }
        
        String frutas[] = {"Banana", "Pera", "Durazno"};  // Trabajamos arreglos con sintaxis resumida
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("frutas "+i +" = "+ frutas[i]);
        }
    }
}
