fn main() {
    println!("Type:      {:>22} {:>22} {:>22} {:>22} {:>22} {:>22} {:>22} {:>22}",
             "i8",
             "i16",
             "i32",
             "i64",
             "u8",
             "u16",
             "u32",
             "u64");
    println!("min_value: {:>22} {:>22} {:>22} {:>22} {:>22} {:>22} {:>22} {:>22}",
             i8::min_value(),
             i16::min_value(),
             i32::min_value(),
             i64::min_value(),
             u8::min_value(),
             u16::min_value(),
             u32::min_value(),
             u64::min_value());
    println!("max_value: {:>22} {:>22} {:>22} {:>22} {:>22} {:>22} {:>22} {:>22}",
             i8::max_value(),
             i16::max_value(),
             i32::max_value(),
             i64::min_value(),
             u8::max_value(),
             u16::max_value(),
             u32::max_value(),
             u64::min_value());
}

