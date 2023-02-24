package com.mycompany.matriu_prova;

import java.util.*;

public class Matriu_prova {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        final int NUM_XIQUETS;
        final int NUM_REGALS;
        System.out.println("Quants xiquets hi han?");
        NUM_XIQUETS = teclado.nextInt();
        System.out.println("Quants regals hi han?");
        NUM_REGALS = teclado.nextInt();
        String regals [][] = new String [NUM_XIQUETS][NUM_REGALS];
        for (int xiquet = 0; xiquet < regals.length; xiquet++) {
            for (int regal = 0; regal < regals[0].length; regal++) {
                System.out.println("Quin regal te cada xiquet?");
                regals[xiquet][regal] = teclado.next();
            }
        }
        
        System.out.println("Que niño quieres buscar?");
        int niño_busqueda = teclado.nextInt();
        for (int i = 0; i < regals[0].length; i++) {
            System.out.println(regals[niño_busqueda][i]);
        }
        
        for (int i = 0; i < regals.length; i++) {
            System.out.println(regals[i][regals[0].length-1]);
        }
        
        for (int xiquet = 0; xiquet < regals.length; xiquet++) {
            System.out.println("Xiquet "+xiquet);
            for (int regal = 0; regal < regals[0].length; regal++) {
                System.out.println("regal "+regal+" : "+regals[xiquet][regal]);
            }
        }
        
        for (int regal = 0; regal < regals[0].length; regal++) {
            System.out.println("Regal "+regal);
            for (int xiquet = 0; xiquet < regals.length; xiquet++) {
                System.out.println("xiquet "+xiquet+" : "+regals[xiquet][regal]);   
            }
        }
    }
}