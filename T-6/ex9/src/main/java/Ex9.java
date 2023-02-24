import java.util.*;

public class Ex9 {

    public static void main(String[] args) {
        Scanner teclat = new Scanner(System.in);
        
        int nota;
        System.out.println("Disme la nota");
        nota = teclat.nextInt();
        
        switch (nota) {
            case 0:
            case 1:
            case 2:
            case 3:
            case 4:
                System.out.println("Insuficiente");
                break;
            case 5:
                System.out.println("Suficiente");
                break;
            case 6:
                System.out.println("Bien");
                break;
            case 7:
            case 8:
                System.out.println("Notable");
                break;
            case 9:
            case 10:
                System.out.println("Excelente");
                break;
            default:
                System.out.println("ERROR");
        }
    }
}
