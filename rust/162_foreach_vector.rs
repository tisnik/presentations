fn main() {
    let vector = vec![1, 2, 3, 4, 5];

    println!("vector has {} items", vector.len());

    for item in vector.iter() {
        println!("{}", item);
    }
}

