fn print_slice(slice :&[i32]) {
    print!("[");
    for i in slice {
        print!("{} ", i);
    }
    println!("]");
}

fn main() {
    let array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let array2 = [1; 10];
    let vector:Vec<_> = (0..10).collect();

    print_slice(&array1);
    print_slice(&array2);
    print_slice(&vector);
}

