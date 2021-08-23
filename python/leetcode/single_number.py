from typing import List


def single_number(nums: List[int]) -> int:
    m = {}
    for i in nums:
        try:
            m.pop(i)
        except:
            m[i] = 1
    return m.popitem()[0]


def main():
    nums_1 = [2, 2, 1]
    assert single_number(nums_1) == 1
    print(single_number(nums_1))
    nums_2 = [4, 1, 2, 1, 2]
    assert single_number(nums_2) == 4
    print(single_number(nums_2))
    nums_3 = [1]
    assert single_number(nums_3) == 1
    print(single_number(nums_3))


if __name__ == '__main__':
    main()
