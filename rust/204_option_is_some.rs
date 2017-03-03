fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x/y)
    } else {
        None
    }
}

fn div_and_print(x: i32, y :i32) {
    let result = div(x, y);
    println!("{:?}", result);

    if result.is_some() {
        println!("{} / {} = {}", x, y, result.unwrap());
    } else {
        println!("Divide by zero");
    }

    println!("");
}

fn main() {
    div_and_print(2, 1);
    div_and_print(2, 0);
}

