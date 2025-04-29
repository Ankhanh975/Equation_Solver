import java.util.Scanner;

public class Lab02_P02 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] f = new int[100001];
        for (int i = 0; i <= n; i++) {
            f[i] = 0;
        }
        for (int i = 2; i <= n; i++) {
            if (f[i] == 0) {
                System.out.print(i + " ");
            }
            int j = i;
            while (j <= n) {
                f[j] = 1;
                j += i;
            }
        }
        scanner.close();
    }
}
