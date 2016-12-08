enum Item {
    First,
    Second,
}

fn select_item(first_item:i32, second_item:i32, item:Item) -> i32 {
    match item {
        Item::First  => first_item,
        Item::Second => second_item,
    }
}

fn main() {
    let x = 10;
    let y = 20;
    println!("1st item = {}", select_item(x, y, Item::First));
    println!("2nd item = {}", select_item(x, y, Item::Second));
    
}

