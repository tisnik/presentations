fn main() {
    let vector:Vec<_> = (0..10).collect();

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }
}

