import java.util.*;

public class Ex16 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num, max = 0;
 
        for (int i = 1; i < 11; i++) {
            System.out.print(i + " Ingrese un numero: ");
            num = in.nextInt();
            if (num > max) {
                max = num;
            }
        }
        System.out.println("Numero Maximo: " + max);
    }
}