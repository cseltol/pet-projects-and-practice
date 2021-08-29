use std::io;


fn main() {
    let mut input = String::new();
    println!("Fib(n), n = ");
    
    io::stdin().read_line(&mut input)
        .expect("Something went wrong while reading user input");
    let n: i64 = input.trim_end_matches("\n").parse()
        .expect("Something went wrong while parsing number from input");

    println!("Fib({})={}", n, fib(n))
}


fn fib(n: i64) -> i64 {
    if n == 0 {
        0
    } else if n == 1 {
        1
    } else {
        fib(n - 1) + fib(n -2)
    }
}