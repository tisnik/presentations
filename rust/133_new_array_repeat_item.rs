fn main() {
    let array = [1; 10];

    println!("array has {} items", array.len());

    for i in 0..array.len() {
        println!("item #{} = {}", i+1, array[i]);
    }
}

