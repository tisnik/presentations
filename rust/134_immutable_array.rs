fn main() {
    let array = [10, 20, 30, 40];

    array[1] = 42;

    for i in 0..array.len() {
        println!("item #{} = {}", i+1, array[i]);
    }
}

