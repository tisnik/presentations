struct Complex {
    real: f32,
    imag: f32,
}


impl Complex {
    fn zero() -> Complex {
        Complex{real:0.0, imag:0.0}
    }

    fn one() -> Complex {
        Complex{real:1.0, imag:0.0}
    }

    fn abs(&self) -> f32 {
        (self.real * self.real + self.imag * self.imag).sqrt()
    }

    fn sqr(&self) -> Complex {
        Complex{real: self.real * self.real - self.imag * self.imag,
                imag: 2.0*self.real * self.imag}
    }

    fn add(&self, c:&Complex) -> Complex {
        Complex{real: self.real + c.real, imag: self.imag + c.imag}
    }

    fn mul(&self, c:&Complex) -> Complex {
        Complex{real: self.real * c.real - self.imag * c.imag, imag: self.real * c.imag + self.imag * c.real}
    }

    fn print(&self) {
        println!("complex number: {}+{}i", self.real, self.imag);
    }
}

fn main() {
    let c1 = Complex::zero();
    let c2 = Complex::one();
    let c3 = c1.add(&c2);
    let c4 = c2.mul(&c2);
    c1.print();
    c2.print();
    c3.print();
    c4.print();
}

