fn main() {
    let mut vector = vec![];

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

