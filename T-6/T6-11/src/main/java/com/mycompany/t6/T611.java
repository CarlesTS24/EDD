package com.mycompany.t6;

import java.util.*;

public class T611 {

    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        boolean ixir = false;
        int opcio;

        ArrayList<String> amics = new ArrayList();

        while (!ixir) {

            System.out.println("1. Introduir un amic");
            System.out.println("2. Esborrar un amic");
            System.out.println("3. Mostrar llista");
            System.out.println("4. Mostrar per inicial");
            System.out.println("5. Modificar amic");
            System.out.println("6. Ordenar alfabeticament");
            System.out.println("7. Buidar la llista");
            System.out.println("8. Ixir");

            System.out.println("Elegix una opcio");
            opcio = sn.nextInt();
            sn.nextLine();

            switch (opcio) {
                case 1:
                    String nom_aña = " ";
                    System.out.println("Com es diu el amic que vols añadir?");
                    nom_aña = sn.nextLine();
                    amics.add(nom_aña);
                    break;
                case 2:
                    String nom_eli = " ";
                    System.out.println("Com es diu el amic que vols eliminar?");
                    nom_eli = sn.nextLine();
                    amics.remove(nom_eli);
                    break;
                case 3:
                    System.out.println("3");
                    break;
                case 4:
                    System.out.println("4");
                    break;
                case 5:
                    System.out.println("5");
                    break;
                case 6:
                    System.out.println("6");
                    break;
                case 7:
                    System.out.println("7");
                    break;
                case 8:
                    char out;
                    System.out.println("Estas segur de que vols ixir?(S/s o N/n)");
                    out = sn.next().charAt(0);
                    if (out == 'S' || out == 's') {
                        ixir = true;
                    }
                    break;
                default:
                    System.out.println("Solo números entre 1 y 8");
            }
        }
    }
}
