fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x/y)
    } else {
        Err("Divide by zero!")
    }
}

fn print_div_result(result: Result<i32, &'static str>) {
    if result.is_err() {
        println!("Result is incorrect");
    }
    else {
        println!("Result is correct");
    }
}

fn main() {
    let z1 = div(2, 1);
    print_div_result(z1);

    let z2 = div(2, 0);
    print_div_result(z2);
}

