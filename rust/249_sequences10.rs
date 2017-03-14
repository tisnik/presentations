use std::collections::VecDeque;

fn print_deque(deque: &VecDeque<i32>) {

    if deque.is_empty() {
        print!("deque is empty");
    } else {
        print!("deque has {} items: ", deque.len());
    }

    for item in deque.iter() {
        print!("{:2} ", item);
    }

    println!("");
}

fn main() {
    let mut deque: VecDeque<i32> = VecDeque::new();

    for i in 0..5 {
        deque.push_front(i);
        print_deque(&deque);
    }

    for i in 10..20 {
        deque.pop_front();
        deque.push_front(i);
        print_deque(&deque);
    }

    for _ in 0..6 {
        deque.pop_front();
        print_deque(&deque);
    }

}

