fn mutate_variable(mut arg1:i32, arg2:&mut i32) {
    println!("mutation ...");
    let x = arg1 * 2;
    arg1  = x;
    *arg2 = arg1;
}

fn print_variables(arg1:i32, arg2:i32) {
    println!("function print_variables()");
    println!("Variable1: {}", arg1);
    println!("Variable2: {}", arg2);
}

fn pass_by_reference(arg1:&i32, arg2:&i32) {
    println!("function pass_by_reference()");
    println!("Variable1: {}", *arg1);
    println!("Variable2: {}", *arg2);
}

fn main() {
    let variable1 = 1;
    let mut variable2 = 1;

    print_variables(variable1, variable2);
    pass_by_reference(&variable1, &variable2);

    mutate_variable(variable1, &mut variable2);

    print_variables(variable1, variable2);
    pass_by_reference(&variable1, &variable2);
}

