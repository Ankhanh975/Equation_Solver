public class gri{
    static int x = 10;

    static {
        System.err.println(101);
        x = 20;
    }
    static {
        System.err.println(102);
        x = 30;
    }
    public static void main(String[] args) {
        System.err.println("");
        System.err.println(x);
    }
}