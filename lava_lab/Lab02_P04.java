import java.util.Scanner;

public class Lab02_P04 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            int n;
            n = scanner.nextInt(); // Size of the sequence
            // n = 5;
            int[] input_array = new int[n];
            int[] new_array_by_index = new int[n];
            for (int i = 0; i < n; i++) {
                input_array[i] = scanner.nextInt();
                new_array_by_index[i] = 0;
            }
            int is_condition_true = 1;
            for (int elem : input_array) {
                int index = elem - 1;
                if (index < n && index >= 0) {
                    new_array_by_index[index] = 1;
                } else {
                    is_condition_true = 0;
                }
            }
            for (int elem : new_array_by_index) {
                if (elem != 1) {
                    is_condition_true = 0;
                }
            }
            System.out.print(is_condition_true);

        }
        scanner.close();
    }
}
