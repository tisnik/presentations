class Loops {
    public static void main(String[] args) throws Exception {
        int i = 1;

        do {
            System.out.println(i);
            i++;
        } while (i<=10);

        i=1;
        while (i <= 10) {
            System.out.println(i);
            i++;
        }

        for (i=0; i<10; i++) {
            System.out.println(i);
        }
    }
}

