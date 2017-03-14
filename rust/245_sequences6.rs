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
    let mut list1: LinkedList<i32> = LinkedList::new();
    let mut list2: LinkedList<i32> = LinkedList::new();

    for _ in 0..10 {
        list1.push_back(1);
    }

    for _ in 0..10 {
        list2.push_front(2);
    }

    println!("1st list");
    print_list(&list1);

    println!("2nd list");
    print_list(&list2);

    list1.append(&mut list2);

    println!("after append");

    println!("1st list");
    print_list(&list1);

    println!("2nd list");
    print_list(&list2);

}

