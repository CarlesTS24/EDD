package com.mycompany.prueba;

public class Prueba {

    public static void main(String[] args) {
        int a;
        a=4;
        int b;
        b=5;
        int c;
        c=6;
        
        a = b++ - c--;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        
        a += --b;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        
        c *= a-- + b;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
              
              
    }
}
