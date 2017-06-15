// balicek gcc zajisti preklad a vytvoreni knihovny za nas
extern crate gcc;

fn main() {
    // preklad a vytvoreni knihovny
    gcc::compile_library("libffi5.a", &["src/ffi5.c"]);
}
