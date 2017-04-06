use std::collections::HashSet;
use std::hash::Hash;
use std::hash::Hasher;

#[derive(Clone)]
struct Complex {
    real: i32,
    imag: i32,
}

impl Complex {
    fn new(real: i32, imag: i32) -> Complex {
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

impl PartialEq for Complex {
    fn eq(&self, right: &Complex) -> bool {
        self.real == right.real && self.imag == right.imag
    }
}

impl Eq for Complex {
}

impl Hash for Complex {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.real.hash(state);
        self.imag.hash(state);
    }
}

fn print_set(set: &HashSet<Complex>) {

    if set.is_empty() {
        println!("set is empty");
    } else {
        println!("set has {} items", set.len());
    }

    for item in set.iter() {
        item.print();
    }
}

fn main() {
    let set: HashSet<Complex> = vec![Complex::new(0, 0),
                                      Complex::new(1, 1),
                                      Complex::new(0, 0),
                                      Complex::new(1, 1),
                                      Complex::new(2, 2),
                                      Complex::new(2, 2)].iter().cloned().collect();

    print_set(&set);

    println!("exit from main()");
}

