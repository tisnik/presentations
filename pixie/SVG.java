public class SVG {

    private static final int GFX_WIDTH = 480;

    private static final int GFX_HEIGHT = 480;

    public static void main(String[] args) {

        // vypocet barvovych slozek pixelu
        int red =    0xff;
        int green =  0xff;
        int blue =   0x00;

        System.out.println("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" width=\"480\" height=\"480\" >");
        for (int i = 0; i < 140; i++) {
            final int radius = 140 - i;
            final int x = (GFX_WIDTH >> 1)  + (int)((i  + 80) * Math.cos(i/12.0));
            final int y = (GFX_HEIGHT >> 1) + (int)((i  + 80) * Math.sin(i/12.0));
            String c = String.format("#%02x%02x%02x", red, green, blue);
            System.out.println("<circle cx='" + x + "'" + " cy='" + y + "'" + " r='" + radius + "' fill='" + c + "' style='fill-opacity:0.06'/>");
            System.out.println("<circle cx='" + x + "'" + " cy='" + y + "'" + " r='" + radius + "' stroke='black' fill='none'/>");
            red-=2;
            blue+=2;
        }
        System.out.println("</svg>");
    }
}

