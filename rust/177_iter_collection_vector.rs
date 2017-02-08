fn main() {
    let array  = [1, 2, 3, 4, 5];
    let vector:Vec<_> = array.iter().collect();

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }
}

