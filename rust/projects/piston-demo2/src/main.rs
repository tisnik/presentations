extern crate piston_window;
use piston_window::*;


fn create_window(width: u32, height: u32) -> PistonWindow {
    let opengl = OpenGL::V2_1;

    let window_size: Size = Size {
        width: width,
        height: height,
    };

    WindowSettings::new("piston-demo2", window_size)
        .exit_on_esc(true)
        .opengl(opengl)
        .build()
        .unwrap()
}


fn on_event(window: &mut PistonWindow, event: Event) -> () {
    window.draw_2d(&event,
                   |_, g2d| { clear([0.8, 1.0, 0.8, 1.0], g2d); });
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
