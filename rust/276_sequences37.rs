use std::collections::LinkedList;

fn print_list(list: &LinkedList<&str>) {

    if list.is_empty() {
        println!("list is empty");
    } else {
        println!("list has {} items", list.len());
    }

    for item in list.iter() {
        println!("{}", item);
    }

    println!("-------------------------");
}

fn main() {
    let list: LinkedList<&str> = vec!["podporucik", "inspektor", "praktikant", "tovarnik"].iter().cloned().collect();

    print_list(&list);
}

