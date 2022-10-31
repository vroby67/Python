import java.util.Scanner;

public class MyClass {
    public static void main(String args[]) {
         //Esercizio 2
        Scanner scan = new Scanner(System.in);
        double n=0;
        n = Double.valueOf(scan.next());
/*        for (int i=0;i<n*10;i+=1)
        {
            System.out.println(i);
        }*/
        for (int i=1;i<=10;i++)
        {
            
            System.out.println(i*n);
        }
    }
}