use std::fmt::Debug;

/// <T: ...> is a Trait Bounding or limitations for type T 

#[derive(Debug)]
struct Point<T: PartialEq> {
    x: T,
    y: T,
}

fn is_eq<T: PartialEq>(item_1: T, item_2: T) -> bool {
    item_1 == item_2
}

fn display<T: Debug>(item: &T) {
    println!("Item : {:#?}", item);
}

/// Eq and PartialEq are traits for == and != operators.
/// Ord and PartialOrd are traits for <, <=, > and >= operators.
impl<T: PartialEq> PartialEq for Point<T> {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

trait Printable<T: Debug> {
    fn print_two_items(item_1: &T, item_2: &T) {
        println!("Item 1 : {:?}", item_1);
        println!("Item 2 : {:?}", item_2);
    }
}

fn main() {
    is_eq(1, 1);
    is_eq(2.1, 3.1);
    is_eq("dev".to_string(), "qa".to_string());

    let p1 = Point {x: 1, y: 2};
    let p2 = Point {x: 2, y: 2};

    display(&1);
    display(&p1);

    let result = p1 == p2;

    let p3 = Point {x: 3, y: 3};
    let p4 = Point {x: 4, y: 4};
    let p5 = Point {x: 3, y: 3};
    let p6 = Point {x: 4, y: 4};

    let complex_p1 = Point{x: p3, y: p4};
    let complex_p2 = Point{x: p5, y: p6};
    let result = complex_p1 == complex_p2;
}
