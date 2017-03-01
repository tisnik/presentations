fn div(x: i32, y: i32) -> Result<i32, &'static str> {
    if y != 0 {
        Ok(x/y)
    } else {
        Err("Divide by zero!")
    }
}

fn print_div_result(result: Result<i32, &'static str>) {
    match result {
        Ok(value)  => println!("value: {}", value),
        Err(error) => println!("error: {}", error)
    }
}

fn translate(s: &'static str) -> &'static str {
    if s == "Divide by zero!" {
        "Deleni nulou"
    }
    else {
        "Neznama chyba"
    }
}

fn main() {
    let z0 = div(0, 1);
    print_div_result(z0);
    print_div_result(z0.map_err(translate));

    let z1 = div(2, 1);
    print_div_result(z1);
    print_div_result(z1.map_err(translate));

    let z2 = div(2, 0);
    print_div_result(z2);
    print_div_result(z2.map_err(translate));
}

