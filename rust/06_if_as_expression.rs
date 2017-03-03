fn if_expression(value:i32) {
    let value_type =
        if value < 0 {
            "zaporna"
        } else {
            if value == 0 {
                "nulova"
            } else {
                "kladna"
            }
        };
    println!("Hodnota {} je {}", value, value_type);
}
 
fn main() {
    if_expression(0);
    if_expression(10);
    if_expression(-10);
}

