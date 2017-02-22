fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x/y)
    }
    else {
        None
    }
}

fn div_message(x: i32, y :i32) -> String {
    let result = div(x, y);

    if let Some(val) = result {
        format!("{} / {} = {}", x, y, val)
    }
    else {
        String::from("Divide by zero")
    }
}

fn main() {
    println!("{}", div_message(2, 1));
    println!("{}", div_message(2, 0));
}

