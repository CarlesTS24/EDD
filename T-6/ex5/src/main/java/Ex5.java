import java.util.Scanner;

public class Ex5 {

    public static void main(String[] args) {
        Scanner teclat = new Scanner(System.in);
        String nom;
        int unitats;
        float preu; // en euros
        
        System.out.println("Quantes unitats has comprat?");
        unitats = teclat.nextInt();
        teclat.nextLine();
        
        System.out.println("Quin es el producte que has comprat?");
        nom = teclat.nextLine();
        
        System.out.println("Quin es el preu del producte?");
        preu = teclat.nextFloat();
        
        System.out.println("Has comprat " +unitats+ " " +nom+ " a " +preu+ " la unitat, són " +(unitats*preu)+ "€" );
    }
}
