import java.util.*;

public class Ex17 {

    public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int num, max = 0, min = 0;
    float total = 0;
    float mitjana = 0;
 
    for (int i = 1; i < 11; i++) {
        System.out.print(i + " Ingrese un numero: ");
        num = in.nextInt();
        if (min != 0 && max != 0) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
 
        if(min==0 || max==0) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        total += num;
    }
    mitjana = total / 10;
    System.out.println("Numero Maximo: " + max);
    System.out.println("Numero Minimo: " + min);
    System.out.println("Numero Mig: " + mitjana);
    }
}
