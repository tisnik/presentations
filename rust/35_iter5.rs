fn main() {
    // iterator (povsimnete si, ze je nemenny)
    let iter = 1..11;

    // promenna pouzita pro vypocet delky sekvence (typ musi byt nastaven na usize)
    let cnt :usize;

    cnt = iter.count();

    println!("count = {}", cnt);
}

