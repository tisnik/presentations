fn main() {
    let mut vector = Vec::with_capacity(10);

    vector.push(10.0);
    vector.push(10);

    println!("vector has {} items", vector.len());
}

