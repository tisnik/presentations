use std::collections::LinkedList;

fn print_list(list: &LinkedList<i32>) {

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
    let mut list: LinkedList<i32> = LinkedList::new();

    println!("new list");
    print_list(&list);

    for i in 0..10 {
        list.push_back(i);
    }

    println!("after 10x push_back");
    print_list(&list);

    for i in 0..10 {
        list.push_front(i);
    }

    println!("after 10x push_front");
    print_list(&list);

    for _ in 0..4 {
        list.pop_front();
    }

    println!("after 5x pop_front");
    print_list(&list);

    for _ in 0..4 {
        list.pop_back();
    }

    println!("after 5x pop_back");
    print_list(&list);

}

