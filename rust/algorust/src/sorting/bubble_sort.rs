pub fn bubble_sort<T: Ord>(arr: &mut [T]) {
    for _i in 0..arr.len() {
        for j in 0..arr.len() - 1 {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn descending() {
        let mut v_1 = vec![6, 5, 4, 3, 2, 1];
        bubble_sort(&mut v_1);
        for i in 0..v_1.len() - 1 {
            assert!(v_1[i] <= v_1[i + 1]);
        }
    }

    #[test]
    fn ascending() {
        // Pre-sorted vector
        let mut v_2 = vec![1, 2, 3, 4, 5, 6];
        bubble_sort(&mut v_2);
        for i in 0..v_2.len() - 1 {
            assert!(v_2[i] <= v_2[i + 1]);
        }
    }
}