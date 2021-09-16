use std::f64::consts::PI;

trait Default {
    fn default() -> Self;
}

struct Point {
    x: f64,
    y: f64,
}

impl Default for Point {
    fn default() -> Point {
        Point {
            x: 0.,
            y: 0.,
        }
    }
}

struct Circle {
    center: Point,
    radius: f64,
}

impl Default for Circle {
    fn default() -> Circle {
        Circle {
            center: Point::default(),
            radius: 1.
        }
    }
}

fn make_default<T: Default>() -> T {
    T::default()
}

fn main() {
    let c: Circle = make_default();
    println!("x = {}, y = {}, radius = {}", c.center.x, c.center.y, c.radius);
}
