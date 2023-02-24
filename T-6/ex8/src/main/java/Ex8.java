import java.io.*;

public class Ex8 {

    public static void main(String[] args) throws IOException {
        BufferedReader teclat = new BufferedReader(new InputStreamReader(System.in));
        float nota;
        
        System.out.println("Disme la nota");
        nota = Float.parseFloat(teclat.readLine() );
        
        if (nota < 0 || nota > 10)
            System.out.println("Error");
        else
            if (nota < 5)
                System.out.println("Ins");
            else
                if (nota < 6)
                    System.out.println("Suf");
                else
                    if (nota < 7)
                        System.out.println("Bé");
                    else
                        if (nota < 9)
                            System.out.println("Not");
                        else
                            System.out.println("Exc");                       
    }
}
