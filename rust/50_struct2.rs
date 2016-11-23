struct Complex {
    real: f32,
    imag: f32,
}

fn main() {
    // nezalezi na poradi inicializace prvku
    let c1 = Complex{imag:0.0, real:0.0};
    println!("complex number: {}+{}i", c1.real, c1.imag);
}

