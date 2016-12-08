struct Complex<T> {
    real: T,
    imag: T,
}

fn main() {
    let c1 = Complex{real:10, imag:20};
    let c2 = Complex{real:10.1, imag:20.1};
    let c3 = Complex{real:10.2f64, imag:20.2f64};
    let c4 = Complex{real:true, imag:false};

    println!("{}+{}i", c1.real, c1.imag);
    println!("{}+{}i", c2.real, c2.imag);
    println!("{}+{}i", c3.real, c3.imag);
    println!("{}+{}i", c4.real, c4.imag);
}

