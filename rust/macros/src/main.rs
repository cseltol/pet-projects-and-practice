macro_rules! might_print {
    ($item:expr) => {
        println!("You gave me a: {:?}.", $item);
    };
}

macro_rules! check {
    ($input:ident, $input2:expr) => {
        println!("Is {:?} equals to {:?}?\nIt's {}.",
            $input, $input2, $input == $input2,
        );
    };
}

fn main() {
    let x = 42;
    let v = vec![1, 2, 3];
    let s = String::from("hello");
    let s_2 = "world";

    check!(x, 42);
    check!(v, vec![1, 2, 3]);
    check!(x, 92);

    might_print!(x);
    might_print!(v);
    might_print!(s);
    might_print!(s_2);
}
