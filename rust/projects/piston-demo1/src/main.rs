extern crate piston_window;
use piston_window::*;


fn create_window() -> PistonWindow {
    let opengl = OpenGL::V2_1;

    WindowSettings::new("piston-demo1", (400, 300))
        .opengl(opengl)
        .build()
        .unwrap()
}


fn on_event(window: &mut PistonWindow, event: Event) -> () {
    window.draw_2d(&event,
                   |context, g2d| { clear([0.8, 1.0, 0.8, 1.0], g2d); });
}


fn event_loop(mut window: PistonWindow) -> () {
    while let Some(event) = window.next() {
        on_event(&mut window, event)
    }
}


fn main() {
    let window: PistonWindow = create_window();
    event_loop(window);
}
