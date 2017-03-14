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

    println!("indexing vector items");
    for i in 0..vector.len() {
        println!("{}", vector[i]);
    }

}

