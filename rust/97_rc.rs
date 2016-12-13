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

}

impl Drop for Complex {
    fn drop(&mut self) {
        println!("Dropping complex number: {:}+{:}i", self.real, self.imag);
    }
}

fn fn2() {
    println!("fn2 begin");
    let c = Box::new(Complex::new(2.0, 2.0));
    println!("fn2 end");
}

fn fn1() {
    println!("fn1 begin");
    let c = Box::new(Complex::new(1.0, 1.0));
    fn2();
    println!("fn1 end");
}

fn main() {
    println!("main begin");
    let c = Rc::new(Complex::new(0.0, 0.0));
    fn1();
    println!("main end");
}

