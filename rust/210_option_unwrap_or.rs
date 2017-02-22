fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x/y)
    }
    else {
        None
    }
}

fn div_print(x: i32, y :i32) -> String {
    let result = div(x, y).unwrap_or(0);

    format!("{} / {} = {}", x, y, result)
}

fn main() {
    println!("{}", div_print(2, 1));
    println!("{}", div_print(2, 0));
}

