use std::rc::Rc;

struct Developer {
    lang: String,
    exp: i32,
}

struct Project {
    name: String,
    dev: Rc<Developer>,
}

// Rc<T> (Reference Counting)
fn main() {
    let dev = Developer {
        lang: "Rust".to_string(),
        exp: 1,
    };

    let d: Rc<Developer> = Rc::new(dev);

    println!("Reference count := {}", Rc::strong_count(&d));

    let google_maps = Project {
        name: "Google Maps".to_string(),
        dev: Rc::clone(&d),
    };

    println!("Reference count := {}", Rc::strong_count(&d));

    let google_pay = Project {
        name: "Google Pay".to_string(),
        dev: Rc::clone(&d),
    };

    println!("Reference count := {}", Rc::strong_count(&d));

    let x = Rc::new(42);
    assert_eq!(Rc::try_unwrap(x), Ok(42));
}