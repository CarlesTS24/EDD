import java.io.*;

public class Ex6 {

    public static void main(String arg[]) {
        BufferedReader teclat = new BufferedReader(new InputStreamReader(System.in));
        String nom;
        int edat;
        float pes;
        char genero;
        String generocom;
        
        try {
            System.out.print("Com et diuen? ");
            nom = teclat.readLine();
            
            System.out.print("Quants anys tens?: ");
            edat = Integer.parseInt( teclat.readLine() );
            
            System.out.print("Què peses(en KG)?");
            pes = Float.parseFloat( teclat.readLine() );
            
            System.out.print("Què genero tienes? (h/d/a)");
            genero = teclat.readLine().charAt(0);
            if(String.valueOf(genero).equals("h")){
                generocom = "home";
            } else {
                if(String.valueOf(genero).equals("d")){
                    generocom = "dona";
                } else {
                    generocom = "altre";
                }
            }
        
            System.out.println("Hola, " + nom + " eres un " + generocom + "!");
            System.out.println("Tens " + edat + " anys i " + pes + " KG.");

        } catch (Exception ex) {
            System.out.println("Ha hagut algun error d'entrada de dades");
        }
    }
}
