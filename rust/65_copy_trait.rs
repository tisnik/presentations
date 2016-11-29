#[derive(Copy, Clone)]
struct Complex {
    real: f32,
    imag: f32,
}

fn print_complex(c:Complex) {
    println!("complex number: {}+{}i", c.real, c.imag);
}

fn main() {
    let c1 = Complex{real:1.0, imag:2.0};
    print_complex(c1);
    let c2 = c1;
    print_complex(c2);
}

