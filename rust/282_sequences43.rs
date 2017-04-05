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

fn print_list(list: &HashSet<Complex>) {

    if list.is_empty() {
        println!("list is empty");
    } else {
        println!("list has {} items", list.len());
    }

    for item in list.iter() {
        item.print();
    }
}

fn main() {
    let list: HashSet<Complex> = vec![Complex::new(0, 0),
                                      Complex::new(1, 1),
                                      Complex::new(2, 2)].iter().cloned().collect();

    print_list(&list);

    println!("exit from main()");
}

