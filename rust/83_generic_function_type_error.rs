enum Item {
    First,
    Second,
}

fn select_item<T>(first_item:T, second_item:T, item:Item) -> T {
    match item {
        Item::First  => first_item,
        Item::Second => second_item,
    }
}

fn main() {
    let x = 10.1;
    let y = 20;
    println!("1st item = {}", select_item(x, y, Item::First));
    println!("2nd item = {}", select_item(x, y, Item::Second));
    
    let z:f32 = 10;
    let w:i32 = 20;
    println!("1st item = {}", select_item(z, w, Item::First));
    println!("2nd item = {}", select_item(z, w, Item::Second));
    
    let a = 10;
    let b = false;
    println!("1st item = {}", select_item(a, b, Item::First));
    println!("2nd item = {}", select_item(a, b, Item::Second));
    
}

