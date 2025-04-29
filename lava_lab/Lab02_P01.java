import java.util.Scanner;

class Operation{
    double GCD(double a, double b) {
        while (a != b) {
            if (a > b) {
                a = a - b;
            } else {
                b = b - a;
            }
        }
        return a;
    }
}

public class Lab02_P01 {
    

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("enter input ");
        int i1, i2;
        i1 = scanner.nextInt();
        i2 = scanner.nextInt();

        Operation operation = new Operation();
        System.out.println(operation.GCD(i1, i2));
    }
}
