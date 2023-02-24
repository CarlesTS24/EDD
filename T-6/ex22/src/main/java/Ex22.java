import java.util.*;
import java.io.*;

public class Ex22 {

    public static void main(String[] args) throws IOException {
        BufferedReader teclat = new BufferedReader(new InputStreamReader(System.in));
        int billetes_de_10, billetes_de_100, billetes_de_20, billetes_de_200, billetes_de_5;
        int billetes_de_50, billetes_de_500, cantitat, monedas_de_1, monedas_de_2;
        System.out.println("Quina cantitat de diners tens?");
        cantitat = Integer.parseInt(teclat.readLine());
        //tambien sirve
        //int queda = cantitat;
        //b500 = queda/500;        
        //queda = queda%500;
        
        monedas_de_1 = cantitat;
        billetes_de_500 = (monedas_de_1-monedas_de_1%500)/500;
        monedas_de_1 = monedas_de_1%500;
        billetes_de_200 = (monedas_de_1-monedas_de_1%200)/200;
        monedas_de_1 = monedas_de_1%200;
        billetes_de_100 = (monedas_de_1-monedas_de_1%100)/100;
        monedas_de_1 = monedas_de_1%100;
        billetes_de_50 = (monedas_de_1-monedas_de_1%50)/50;
        monedas_de_1 = monedas_de_1%50;
        billetes_de_20 = (monedas_de_1-monedas_de_1%20)/20;
        monedas_de_1 = monedas_de_1%20;
        billetes_de_10 = (monedas_de_1-monedas_de_1%10)/10;
        monedas_de_1 = monedas_de_1%10;
        billetes_de_5 = (monedas_de_1-monedas_de_1%5)/5;
        monedas_de_1 = monedas_de_1%5;
        monedas_de_2 = (monedas_de_1-monedas_de_1%2)/2;
        monedas_de_1 = monedas_de_1%2;
        
        System.out.println("Tienes " +billetes_de_500+ " billetes de 500");
        System.out.println("Tienes " +billetes_de_200+ " billetes de 200");
        System.out.println("Tienes " +billetes_de_100+ " billetes de 100");
        System.out.println("Tienes " +billetes_de_50+ " billetes de 50");
        System.out.println("Tienes " +billetes_de_20+ " billetes de 20");
        System.out.println("Tienes " +billetes_de_10+ " billetes de 10");
        System.out.println("Tienes " +billetes_de_5+ " billetes de 5");
        System.out.println("Tienes " +monedas_de_2+ " monedas de 2");
        System.out.println("Tienes " +monedas_de_1+ " monedas de 1");
    }
}
