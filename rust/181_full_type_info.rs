fn main() {
    let array:[f32;5]  = [1., 2., 3., 4., 5.];
    let vector:Vec<f32> = array.iter()
                             .take(10)
                             .map(|&x| 1.0/x)
                             .collect();

    println!("vector has {} items", vector.len());

    for item in &vector {
        println!("{}", item);
    }
}

