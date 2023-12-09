// Bubble Sort
public class ModerateBug {
    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("UnOrdered");
        printArray(array);
        bubbleSort(array);
        System.out.println("Ordered:");
        printArray(array);
    }

    private static void bubbleSort(int[] array) {
        int n = array.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (array[j] > array[j + 1]) {
                    array[j] = array[j + 1];
                    array[j + 1] = array[j];
                }
            }
        }
    }

    private static void printArray(int[] array) {
        for (int j : array) {
            System.out.print(j + " ");
        }
        //
    }
}