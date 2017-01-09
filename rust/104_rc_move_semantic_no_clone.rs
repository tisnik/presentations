use std::rc::Rc;

struct Complex {
    real: f32,
    imag: f32,
}

impl Complex {

    fn new(real: f32, imag: f32) -> Complex {
        println!("Constructing complex number: {:}+{:}i", real, imag);
        Complex{real:real, imag:imag}
    }

    fn print(&self) {
        println!("complex number: {:?}+{:?}i", self.real, self.imag);
    }

}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn f1() -> Rc<Complex> {
    Rc::new(Complex::new(0.0, 0.0))
}

fn f2(c:Rc<Complex>) {
    c.print();
}

fn main() {
    println!("main begin");
    let c = f1();
    c.print();
    f2(c);
    f2(c);
}

