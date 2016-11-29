struct Complex {
    real: f32,
    imag: f32,
}

fn print_complex(c:&Complex) {
    println!("complex number: {}+{}i", c.real, c.imag);
}

fn add_real(c:&mut Complex,real:f32) {
    c.real += real;
}

fn main() {
    let mut c1 = Complex{real:1.0, imag:2.0};
    print_complex(&c1);
    add_real(&mut c1, 41.);
    print_complex(&c1);
}

