macro_rules! unifunc {
    ($x:expr => zero )   => (0);
    ($x:expr => ident)   => ($x);
    ($x:expr => sqr  )   => ($x * $x);
}

fn main() {
    println!("{}", unifunc!(2 => zero));
    println!("{}", unifunc!(2 => ident));
    println!("{}", unifunc!(2 => sqr));

    println!("{}", unifunc!(10 => zero));
    println!("{}", unifunc!(10 => ident));
    println!("{}", unifunc!(10 => sqr));
}

