use std::ops::Add;
use std::ops::AddAssign;
use std::cmp::PartialEq;

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

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn main() {
    let c1 = Complex::new(1.0, 1.0);
    let c2 = Complex::new(3.0, 4.0);
    let c3 = Complex::new(0.0, 0.0);
    c1.print();
    c2.print();
    c3.print();
    c1.drop();
    c2.drop();
    c3.drop();
}

