struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {

    fn new(real: f32, imag: f32) -> Complex {
        Complex{real:real, imag:imag}
    }

    fn new_on_heap(real: f32, imag: f32) -> Box<Complex> {
        Box::new(Complex{real:real, imag:imag})
    }

    fn print(&self) {
        println!("complex number: {}+{}i", self.real, self.imag);
    }

}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn main() {
    let c1 = Box::new(Complex::new(1.0, 2.0));
    let c2 = Complex::new_on_heap(3.0, 4.0);
    c1.print();
    c2.print();
}

