import java.util.Scanner;

public class Lab02_P03 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int[][] A = new int[n][k];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                A[i][j] = scanner.nextInt();
            }
        }
        int _ = scanner.nextInt();
        int m = scanner.nextInt();

        int[][] B = new int[k][m];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < m; j++) {
                B[i][j  ] = scanner.nextInt();
            }
        }
        int[][] C = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                C[i][j] = 0;
                for (int t = 0; t < k; t++) {
                    C[i][j] = C[i][j] + A[i][t] * B[t][j];
                }
            }
        }
        scanner.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(C[i][j]+ " ");
            }
            System.out.println();
        }
    }
}
