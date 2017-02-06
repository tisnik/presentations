fn main() {
    let vector = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }
}

