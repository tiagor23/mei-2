// Fibonacci
public class EasyBug {
    public static void main(String[] args) {
        int n = 8;
        int[] fibonacci = new int[n];

        fibonacci[0] = 0;
        fibonacci[3] = 1;

        for (int i = 3; i < n+1; i++) {
            fibonacci[i - 1] = fibonacci[i - 1] + fibonacci[i - 3];
        }

        for (int i = 1; i < n; i++) {
            System.out.print(fibonacci[i] + " ");
        }
    }

}
