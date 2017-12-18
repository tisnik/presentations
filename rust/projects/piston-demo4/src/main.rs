extern crate piston_window;
use piston_window::*;


fn create_window(width: u32, height: u32) -> PistonWindow {
    let opengl = OpenGL::V2_1;

    let window_size: Size = Size {
        width: width,
        height: height,
    };

    WindowSettings::new("piston-demo4", window_size)
        .exit_on_esc(true)
        .opengl(opengl)
        .samples(4)
        .build()
        .unwrap()
}


fn on_event(window: &mut PistonWindow, event: Event) -> () {
    const RED:   [f32; 4] = [1.0, 0.0, 0.0, 1.0];
    const BLUE:  [f32; 4] = [0.0, 0.0, 1.0, 1.0];
    const SQUARE_SIZE: f64 = 50.0;
    const LINE_BORDER: f64 = 10.0;

    let size = window.window.size();
    let width = size.width as f64;
    let height = size.height as f64;

    let x = (width - SQUARE_SIZE)/2.0;
    let y = (height - SQUARE_SIZE)/2.0;
    let square = rectangle::square(x, y, SQUARE_SIZE);

    let x1 = LINE_BORDER;
    let y1 = LINE_BORDER;

    let x2 = width - LINE_BORDER;
    let y2 = height - LINE_BORDER;

    let line1:[f64;4] = [x1, y1, x2, y2];
    let line2:[f64;4] = [x1, y2, x2, y1];

    window.draw_2d(&event,
                   |context, g2d| { clear([0.8, 1.0, 0.8, 1.0], g2d);
                                    g2d.clear_stencil(0);
                                    line(BLUE, 1., line1, context.transform, g2d);
                                    line(BLUE, 0.5, line2, context.transform, g2d);
                                    rectangle(RED, square, context.transform, g2d); });
}


fn event_loop(mut window: PistonWindow) -> () {
    while let Some(event) = window.next() {
        on_event(&mut window, event)
    }
}


fn main() {
    let window: PistonWindow = create_window(400, 300);
    event_loop(window);
}
