from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    is_solved = False
    answer = []
    i = 0
    while i < len(nums) and not is_solved:
        j = i + 1
        while j < len(nums) and not is_solved:
            if nums[i] + nums[j] == target:
                is_solved = True
                answer.append(i)
                answer.append(j)
                return answer
            j += 1
        i += 1
    return answer


def main():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]
    print(two_sum(nums, target))


if __name__ == '__main__':
    main()
