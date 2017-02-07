fn main() {
    let mut vector : Vec<i8> = Vec::with_capacity(10);

    vector.push(10);
    vector.push(100);
    vector.push(1000);

    println!("vector has {} items", vector.len());
}

