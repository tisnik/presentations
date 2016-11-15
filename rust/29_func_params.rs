fn mutate_variable(arg1:i32, arg2:&mut i32) {
    let x = arg1 * 2;
    *arg2 = x;
}

fn print_variables(arg1:i32, arg2:i32) {
    println!("Variable1: {}", arg1);
    println!("Variable2: {}", arg2);
}

fn main() {
    let variable1 = 1;
    let mut variable2 = 1;

    print_variables(variable1, variable2);
    mutate_variable(variable1, &mut variable2);
    print_variables(variable1, variable2);
}

