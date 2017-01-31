fn main() {
    let array = [10, 20, 30, 40];

    println!("array has {} items", array.len());

    for i in 0..array.len() {
        println!("item #{} = {}", i+1, array[i]);
    }
}

