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

    println!("new list");
    print_list(&list1);

    for i in 0..10 {
        list1.push_back(i);
    }

    println!("after 10x push_back");
    print_list(&list1);

    let list2 = list1.split_off(5);

    println!("1st list");
    print_list(&list1);

    println!("2nd list");
    print_list(&list2);

}

