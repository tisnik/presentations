use std::collections::BinaryHeap;

fn main() {
    let mut heap = BinaryHeap::new();

    heap.push("Trachta");
    heap.push("Hlavacek");
    heap.push("Bierhanzel");
    heap.push("Meyer");
    heap.push("Vaclav Kotek");

    for item in &heap {
        println!("{}", item);
    }
}

