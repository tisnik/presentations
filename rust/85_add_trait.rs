use std::ops::Add;

struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {

    fn new(real: f32, imag: f32) -> Complex {
        Complex{real:real, imag:imag}
    }

    fn print(&self) {
        println!("complex number: {:}+{:}i", self.real, self.imag);
    }

}

impl Add for Complex {

    type Output = Complex;

    fn add(self, right: Complex) -> Self::Output {
        Complex{real: self.real + right.real,
                imag: self.imag + right.imag}
    }

}

fn main() {
    let c1 = Complex::new(1.0, 1.0);
    let c2 = Complex::new(3.0, 4.0);
    c1.print();
    c2.print();
    let c3 = c1 + c2;
    c3.print();
}

