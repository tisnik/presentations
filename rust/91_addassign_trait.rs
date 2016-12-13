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

impl Add<Complex> for Complex {

    type Output = Complex;

    fn add(self, right: Complex) -> Self::Output {
        Complex::new(self.real + right.real,
                     self.imag + right.imag)
    }
}

impl Add<f32> for Complex {

    type Output = Complex;

    fn add(self, right: f32) -> Self::Output {
        Complex::new(self.real + right,
                     self.imag)
    }
}

impl AddAssign for Complex {
    fn add_assign(&mut self, right: Complex) {
        *self = Complex::new(self.real + right.real,
                             self.imag + right.imag)
    }
}

impl PartialEq for Complex {

    fn eq(&self, right: &Complex) -> bool {
        self.real == right.real && self.imag == right.imag
    }
}

fn main() {
    let c1 = Complex::new(1.0, 1.0);
    let c2 = Complex::new(3.0, 4.0);
    c1.print();
    c2.print();
    let c3 = c1 + c2;
    let c4 = Complex::new(4.0, 5.0);
    c3.print();
    c4.print();
    println!("c3 == c4? {}", (if c3==c4 { "yes"} else {"no"}));

    let mut c6 = Complex::new(1.0, 1.0);
    let c7 = Complex::new(3.0, 4.0);
    c6 += c7;
    c6.print();
}

