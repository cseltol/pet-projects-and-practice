use std::ops::AddAssign;

pub fn generic_counting_sort<T: Into<u64> + From<u8> + AddAssign + Copy>(
    arr: &mut [T],
    maxval: usize,
) {
    let mut occurences: Vec<usize> = vec![0; maxval + 1];

    for &data in arr.iter() {
        occurences[data.into() as usize] += 1;
    }

    let mut data = T::from(0);

    for &number in occurences.iter() {
        for i in 0..number {
            arr[i] = data;
        }
        data += T::from(1);
    }
}

pub fn counting_sort(arr: &mut [u32], maxval: usize) {
    let mut occurences: Vec<usize> = vec![0; maxval + 1];

    for &data in arr.iter() {
        occurences[data as usize] += 1;
    }

    for (data, &number) in occurences.iter().enumerate() {
        for i in 0..number {
            arr[i] = data as u32;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::super::is_sorted;
    use super::*;

    #[test]
    fn counting_sort_descending() {
        let mut ve1 = vec![6, 5, 4, 3, 2, 1];
        counting_sort(&mut ve1, 6);

        assert!(is_sorted(&ve1));
    }

    #[test]
    fn counting_sort_pre_sorted() {
        let mut ve2 = vec![1, 2, 3, 4, 5, 6];
        counting_sort(&mut ve2, 6);

        assert!(is_sorted(&ve2));
    }

    #[test]
    fn generic_counting_sort() {
        let mut ve1: Vec<u8> = vec![100, 30, 60, 10, 20, 120, 1];
        super::generic_counting_sort(&mut ve1, 120);

        assert!(is_sorted(&ve1));
    }

    #[test]
    fn presorted_u64_counting_sort() {
        let mut ve2: Vec<u64> = vec![1, 2, 3, 4, 5, 6];
        super::generic_counting_sort(&mut ve2, 6);

        assert!(is_sorted(&ve2));
    }
}
