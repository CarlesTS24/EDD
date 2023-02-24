import java.util.*;
import javax.swing.JOptionPane;

public class Ex172 {

    public static void main(String[] args) {
        int billetes_de_10, billetes_de_100, billetes_de_20, billetes_de_200, billetes_de_5;
        int billetes_de_50, billetes_de_500, cantidad_de_euros, monedas_de_1, monedas_de_2;
        cantidad_de_euros = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el valor de cantidad de euros"));
        monedas_de_1=cantidad_de_euros;
        billetes_de_500=(monedas_de_1-monedas_de_1%500)/500;
        monedas_de_1=monedas_de_1%500;
        billetes_de_200=(monedas_de_1-monedas_de_1%200)/200;
        monedas_de_1=monedas_de_1%200;
        billetes_de_100=(monedas_de_1-monedas_de_1%100)/100;
        monedas_de_1=monedas_de_1%100;
        billetes_de_50=(monedas_de_1-monedas_de_1%50)/50;
        monedas_de_1=monedas_de_1%50;
        billetes_de_20=(monedas_de_1-monedas_de_1%20)/20;
        monedas_de_1=monedas_de_1%20;
        billetes_de_10=(monedas_de_1-monedas_de_1%10)/10;
        monedas_de_1=monedas_de_1%10;
        billetes_de_5=(monedas_de_1-monedas_de_1%5)/5;
        monedas_de_1=monedas_de_1%5;
        monedas_de_2=(monedas_de_1-monedas_de_1%2)/2;
        monedas_de_1=monedas_de_1%2;
        JOptionPane.showMessageDialog(null,
            "Valor de billetes de 10: " + billetes_de_10 + "\n" +
            "Valor de billetes de 100: " + billetes_de_100 + "\n" +
            "Valor de billetes de 20: " + billetes_de_20 + "\n" +
            "Valor de billetes de 200: " + billetes_de_200 + "\n" +
            "Valor de billetes de 5: " + billetes_de_5 + "\n" +
            "Valor de billetes de 50: " + billetes_de_50 + "\n" +
            "Valor de billetes de 500: " + billetes_de_500 + "\n" +
            "Valor de monedas de 1: " + monedas_de_1 + "\n" +
            "Valor de monedas de 2: " + monedas_de_2);
    }
}