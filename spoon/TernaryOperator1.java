class TernaryOperator1 {
    public static void main(String[] args) {
        float x = 10.0f;
        //float x = 0.0f;

        float y = (x == 0) ? 0.0f : 1.0f/x;

        System.out.println("x = " + x);
        System.out.println("y = " + y);
    }
}

