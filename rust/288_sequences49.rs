use std::collections::BinaryHeap;

fn main() {
    let mut heap = BinaryHeap::new();

    heap.push(1);
    heap.push(2);
    heap.push(3);
    heap.push(4);
    heap.push(100);
    heap.push(5);
    heap.push(6);
    heap.push(7);
    heap.push(8);

    println!("max value: {:?}", heap.peek());

    for item in &heap {
        println!("{}", item);
    }

    for _ in 0..heap.len()+1 {
        println!("{:?}", heap.pop());
    }

}

