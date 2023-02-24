
import java.io.*;

public class Ex7 {

    public static void main(String[] args) throws IOException {
        BufferedReader teclat = new BufferedReader(new InputStreamReader(System.in));
        float num1;
        float num2;
        float num3;
        
        System.out.println("Disme un numero");
        num1 = Float.parseFloat(teclat.readLine() );
        
        System.out.println("Disme un segon numero");
        num2 = Float.parseFloat(teclat.readLine() );
        
        System.out.println("Disme el tercer numero");
        num3 = Float.parseFloat(teclat.readLine() );
        
        if (num1 < num2)
            if (num2 < num3)
                System.out.println(num3);
            else
                System.out.println(num2);
        else
            if (num3 < num1)
                System.out.println(num1);                         
    }
}
