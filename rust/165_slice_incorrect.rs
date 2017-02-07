fn main() {
    let vector = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    println!("vector has {} items", vector.len());

    let slice = vector[3..7];

    println!("slice has {} items", slice.len());

    for item in slice {
        println!("{}", item);
    }
}

