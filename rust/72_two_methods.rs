struct Complex {
    real: f32,
    imag: f32,
}


impl Complex {
    fn abs(&self) -> f32 {
        (self.real * self.real + self.imag * self.imag).sqrt()
    }

    fn print(&self) {
        println!("complex number: {}+{}i", self.real, self.imag);
    }
}

fn main() {
    let c1 = Complex{real:3.0, imag:4.0};
    c1.print();
    println!("absolute value: {}", c1.abs());
}

