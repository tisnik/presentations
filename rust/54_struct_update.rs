struct Complex {
    real: f32,
    imag: f32,
}

fn main() {
    let c1 = Complex{real:0.0, imag:0.0};
    let c2 = Complex{real:2.0, ..c1};
    let c3 = Complex{..c2};
    println!("complex number 1: {}+{}i", c1.real, c1.imag);
    println!("complex number 2: {}+{}i", c2.real, c2.imag);
    println!("complex number 3: {}+{}i", c3.real, c3.imag);
}

