struct Complex {
    real: f32,
    imag: f32,
}

fn print_complex(c:&Complex) {
    println!("complex number: {}+{}i", c.real, c.imag);
}

fn main() {
    let c1 = Complex{real:1.0, imag:2.0};
    println!("complex number: {}+{}i", c1.real, c1.imag);
    print_complex(&c1);
    println!("complex number: {}+{}i", c1.real, c1.imag);
}

