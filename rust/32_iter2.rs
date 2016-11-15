fn main() {
    // promenna pouzita pro vypocet delky sekvence (naivni implementace)
    let mut cnt :u32 = 0;

    // projiti sekvence hodnot od 1 do 10 (vcetne)
    for i in 1..11 {
        cnt += 1;
    }
    println!("{}", cnt);
}

