struct Complex {
    real: f32,
    imag: f32,
}


impl Complex {
    fn abs(&self) -> f32 {
        (self.real * self.real + self.imag * self.imag).sqrt()
    }

    fn sqr(&self) -> Complex {
        Complex{real: self.real * self.real - self.imag * self.imag,
                imag: 2.0*self.real * self.imag}
    }

    fn print(&self) {
        println!("complex number: {}+{}i", self.real, self.imag);
    }
}

fn main() {
    let c1 = Complex{real:1.0, imag:0.0};
    let c2 = Complex{real:0.0, imag:2.0};
    let c3 = Complex{real:2.0, imag:2.0};
    let c4 = c1.sqr();
    let c5 = c2.sqr();
    let c6 = c3.sqr();
    c1.print();
    c2.print();
    c3.print();
    c4.print();
    c5.print();
    c6.print();
}

