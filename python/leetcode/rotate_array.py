def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

def main():
    res_1 = rotate([1, 2, 3, 4, 5, 6, 7], 3)
    res_2 = rotate([-1, -100, 3, 99], 2)
    assert res_1 == [5, 6, 7, 1, 2, 3, 4]
    print(res_1)
    assert res_2 == [3, 99, -1, -100]
    print(res_2)


if __name__ == '__main__':
    main()
