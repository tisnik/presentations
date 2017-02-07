fn main() {
    let mut vector = Vec::with_capacity(10);

    println!("vector has capacity for {} items", vector.capacity());
    println!("vector has {} items", vector.len());

    for i in 0..10 {
        vector.push(2*i);
    }

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }

    for _ in 0..5 {
        vector.pop();
    }

    println!("-------------------------");

    for item in &vector {
        println!("{}", item);
    }

}

