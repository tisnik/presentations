#[derive(Debug)]
enum DivError {
    DivideByZero,
    DivideZeroByZero
}

fn div(x: i32, y: i32) -> Result<i32, DivError> {
    if y != 0 {
        Ok(x/y)
    } else if x != 0 {
        Err(DivError::DivideByZero)
    } else {
        Err(DivError::DivideZeroByZero)
    }
}

fn print_div_result(result: Result<i32, DivError>) {
    match result {
        Ok(value)  => println!("value: {}", value),
        Err(error) => println!("error: {:?}", error)
    }
}

fn main() {
    let z0 = div(0, 1);
    print_div_result(z0);

    let z1 = div(2, 1);
    print_div_result(z1);

    let z2 = div(2, 0);
    print_div_result(z2);

    let z3 = div(0, 0);
    print_div_result(z3);
}

