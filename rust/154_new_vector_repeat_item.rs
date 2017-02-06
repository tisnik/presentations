fn main() {
    let vector = vec![1; 10];

    println!("vector has {} items", vector.len());

    for i in 0..vector.len() {
        println!("item #{} = {}", i+1, vector[i]);
    }
}

