use std::collections::LinkedList;

fn main() {
    let mut list: LinkedList<i32> = LinkedList::new();

    for i in 5..10 {
        list.push_back(i);
    }

    for i in 0..15 {
        println!("{}: {}", i, list.contains(&i));
    }
}

