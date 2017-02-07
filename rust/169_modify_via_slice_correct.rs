fn main() {
    let mut vector = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    println!("vector has {} items", vector.len());

    {
        let slice = &mut vector[3..7];

        slice[1] = 100;
    }

    for item in &vector {
        println!("{}", item);
    }
}

