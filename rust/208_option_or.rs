fn div(x: i32, y: i32) -> Option<i32> {
    if y != 0 {
        Some(x/y)
    }
    else {
        None
    }
}

fn sqr(val: Option<i32>) -> Option<i32> {
    let x = val.unwrap();
    Some(x*x)
}

fn div_square(x: i32, y :i32) -> String {
    let result = sqr(div(x, y).or(Some(0)));

    if let Some(val) = result {
        format!("({} / {}) ^ 2 = {}", x, y, val)
    }
    else {
        String::from("Divide by zero")
    }
}

fn main() {
    println!("{}", div_square(2, 1));
    println!("{}", div_square(2, 0));
}

