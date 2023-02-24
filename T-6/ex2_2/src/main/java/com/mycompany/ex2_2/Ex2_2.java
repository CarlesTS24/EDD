package com.mycompany.ex2_2;

import java.util.*;

public class Ex2_2 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int q_alu;
        q_alu = 5;
        int expedients [] = new int [q_alu+1];
        float notes [] = new float [q_alu+1];
        int edats [] = new int [q_alu+1];
        
        for (int i = 1; i < expedients.length; i++) {
            System.out.println("Ingrese el numero de expediente:");
            expedients[i] = teclado.nextInt();
            
            System.out.println("Ingrese la nota del alumno:");
            notes[i] = teclado.nextFloat();
            
            System.out.println("Ingrese la edad del alumno:");
            edats[i] = teclado.nextInt();  
        }
        
        System.out.println("EXP   NOTA    EDAT");
        for (int alu = 1; alu < q_alu; alu++) {
            System.out.println(expedients[alu] + "   " + notes[alu] + "  " + edats[alu]);
        }
        
        System.out.println("");
        
    }
}