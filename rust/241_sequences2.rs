fn print_vector(vector: &Vec<i32>) {
    if vector.is_empty() {
        println!("vector is empty");
    } else {
        println!("vector has {} items", vector.len());
    }

    for item in vector.iter() {
        println!("{}", item);
    }

    println!("-------------------------");
}

fn main() {
    let mut vector = vec![];

    println!("new vector");
    print_vector(&vector);

    for i in 0..10 {
        vector.push(2*i);
    }

    println!("after 10x push");
    print_vector(&vector);

    for _ in 0..5 {
        vector.pop();
    }

    println!("after 5x pop");
    print_vector(&vector);

    vector.resize(10, -1);

    println!("after resize to 10 items");
    print_vector(&vector);

    vector.insert(2, 999);
    vector.insert(10, 1000);

    println!("after 2x insert");
    print_vector(&vector);

    vector.remove(0);
    vector.remove(10);

    println!("after 2x remove");
    print_vector(&vector);

}

