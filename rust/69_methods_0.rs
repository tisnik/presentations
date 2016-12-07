struct Complex {
    real: f32,
    imag: f32,
}

fn print_complex(c:&Complex) {
    println!("complex number: {}+{}i", c.real, c.imag);
}

fn abs(c:&Complex) -> f32 {
    (c.real * c.real + c.imag * c.imag).sqrt()
}

fn main() {
    let c1 = Complex{real:3.0, imag:4.0};
    print_complex(&c1);
    println!("absolute value: {}", abs(&c1));
}

