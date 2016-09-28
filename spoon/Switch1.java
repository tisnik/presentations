class Switch1 {
    public static void main(String[] args) throws Exception {
        System.out.println("h: help   f: format disk  q: quit");

        char input = (char)System.in.read();

        switch (input) {
            case 'h': System.out.println("Help ...");
                      break;
            case 'f': System.out.println("Formatting / ...");
                      break;
            case 'q': System.out.println("Good bye ...");
                      break;
        }
        System.out.println(input);

    }
}

