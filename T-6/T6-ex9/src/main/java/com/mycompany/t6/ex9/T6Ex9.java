package com.mycompany.t6.ex9;

import java.util.*;

public class T6Ex9 {

    public static void main(String[] args) {
        String text = teclat.lligString("Text:");

        String[] paraules = text.split(" ");

        int lonMax = 0;
        String parMax = "";
        String parUlt = "";
        for (String p : paraules) {
            
            String descr;
            if (p.equals(p.toUpperCase())) {
                descr = "majúscules";
            } else {
                if (p.equals(p.toLowerCase())) {
                    descr = "minúscules";
                } else {
                    descr = "ni maj ni min";
                }
            }
            System.out.println(p + "\t" + p.length() + "\t" + descr);
            
            if (p.length()>lonMax){
                lonMax = p.length();
                parMax = p;
            }
            
            if (p.compareTo(parUlt)>0){
                parUlt = p;
            }
        }
        System.out.println("Par més llarga: " + parMax + " amb " + lonMax + " lletres");
        System.out.println("Par última: " + parUlt);  
    }
}


