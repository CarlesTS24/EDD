package com.mycompany.act2;

import java.util.*;

public class Act2 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int v1 [] = new int [10];
        int v2 [] = new int [10];
        int num;
        int contador_v2 = 0;
        
        for (int i = 0; i < v1.length; i++) {
            System.out.println("Numero "+(i+1));
            num = teclado.nextInt();
            v1[i] = num;
        }
        
        for (int i = v2.length-1; i >= 0; i--) {
            v2[contador_v2] =v1[i];
            contador_v2++;
        }
        
        for (int i = 0; i < v1.length; i++) {
            System.out.println(v1[i]+ " + " +v2[i]+ " = " +(v1[i]+v2[i]));
        }
    } 
}
