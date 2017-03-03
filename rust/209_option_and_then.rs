fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x/y)
    } else {
        None
    }
}

fn sqr(x: i32) -> Option<i32> {
    Some(x*x)
}

fn div_square(x: i32, y :i32) -> String {
    let result = div(x, y).and_then(sqr);

    if let Some(val) = result {
        format!("({} / {}) ^ 2 = {}", x, y, val)
    } else {
        String::from("Divide by zero")
    }
}

fn main() {
    println!("{}", div_square(2, 1));
    println!("{}", div_square(2, 0));
}

