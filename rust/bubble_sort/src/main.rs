fn main() {
    let mut a = [2, 1, 4, 0, 6, 9];
    bubble_sort(&mut a);
    optimize_bubble_sort(&mut a);
    println!("{:?}", a)
}

/// Base Bubble Sort
fn bubble_sort(arr: &mut [i64]) {
    for i in 0..arr.len() - 1 {
        for j in 0..arr.len() - i - 1 {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
    }
}

/// Optimized Bubble Sort 
fn optimize_bubble_sort(arr: &mut [i64]) {
    let mut new_len: usize;
    let mut len = arr.len();
    loop {
        new_len = 0;
        for i in 1..len {
            if arr[i - 1] > arr[i] {
                arr.swap(i - 1, i);
                new_len = i;
            }
        }
        if new_len == 0 {
            break;
        }
        len = new_len;
    }
}