import java.util.Scanner;

class Funcionetes {
    static Scanner teclat = new Scanner(System.in);
 
    // ----------------------------------------------------------------------------------------
    public static int lligInt(String pregunta) {
        int numero;
        
        do {
            try {
                System.out.println( pregunta );
                numero = teclat.nextInt(); // Si hem posat lletres, va al catch
                // Si passa per ací, no ha donat error. Buidem \n i tornem el número.
                teclat.nextLine();
                return numero;
                
            } catch (Exception e) { // Si hem posat lletres, avisa i buida el buffer:
                System.out.print("Ha de ser un número enter:");
                teclat.nextLine();
            }
        } while (true); // Bucle infinit fins que retornem el número correcte.
    }
    // ----------------------------------------------------------------------------------------
    //public static float lligFloat(String pregunta) {
    //    
    //}
 // ----------------------------------------------------------------------------------------
}