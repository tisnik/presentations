use std::iter::FromIterator;

fn main() {
    let vector = Vec::from_iter(1..10);

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }
}

