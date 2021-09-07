from bubble_sort import bubble_sort


def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    return bubble_sort(nums1)


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))


if __name__ == '__main__':
    main()
