fn main() {
    let mut vector = vec![1; 10];

    println!("vector has {} items", vector.len());

    print!("[");
    for i in 0..vector.len() {
        print!("{} ", vector[i]);
    }
    println!("]");

    vector[5] = 100;

    print!("[");
    for i in 0..vector.len() {
        print!("{} ", vector[i]);
    }
    println!("]");

}

