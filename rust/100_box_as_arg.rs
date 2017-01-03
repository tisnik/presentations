struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {
    fn new(real: f32, imag: f32) -> Complex {
        Complex{real:real, imag:imag}
    }
}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn print_complex(c:Box<Complex>) {
    println!("Complex number: {:}+{:}i", c.real, c.imag);
}

fn main() {
    let c1 = Box::new(Complex::new(1.0, 2.0));
    let c2 = Box::new(Complex::new(1.0, 2.0));
    println!("calling print_complex");
    print_complex(c1);
    println!("back in main");
}

