public class JavaRefefences {
    public static void main(String[] args) {
        Integer i = 12345678;
        Integer j = 12345677;

        System.out.println(i);
        System.out.println(j);
        System.out.println(i==j);

        j++;

        System.out.println(i);
        System.out.println(j);
        System.out.println(i==j);
    }
}


