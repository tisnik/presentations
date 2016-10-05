public class ManyConstructors {
    ManyConstructors() {
    }
    ManyConstructors(int x) {
    }
    ManyConstructors(int x, int y) {
    }
    ManyConstructors(String str) {
    }
    ManyConstructors(String... strs) {
    }
    ManyConstructors(float x) {
        System.out.println(x);
    }
    ManyConstructors(float x, float y) {
        System.out.println(x);
        System.out.println(y);
    }
    private ManyConstructors(double a) {
    }
    protected ManyConstructors(double a, double b) {
    }
    public ManyConstructors(double a, double b, double c) {
    }
}

