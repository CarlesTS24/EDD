
import java.util.*;

public class Ex10 {

    public static void main(String[] args) {
        Scanner teclat = new Scanner(System.in);

        float num1;
        System.out.println("Disme el primer numero");
        num1 = teclat.nextFloat();

        float num2;
        System.out.println("Disme el segon numero");
        num2 = teclat.nextFloat();

        char hacer;
        System.out.println("Que quieres hacer(S s +  R r -  M m * x  D d /)");
        hacer = teclat.next().charAt(0);

        switch (hacer) {
            case 'S':
            case 's':
            case '+':
                System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
                break;
            case 'R':
            case 'r':
            case '-':
                System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
                break;
            case 'M':
            case 'm':
            case '*':
            case 'x':
                System.out.println(num1 + " * " + num2 + " = " + (num1 * num2));
                break;
            case 'D':
            case 'd':
            case '/':
                System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
                break;
            default:
                System.out.println("ERROR");
        }
    }
}
