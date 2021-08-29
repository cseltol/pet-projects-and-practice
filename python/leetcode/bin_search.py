from random import randrange


def bin_search(arr, left, right, target):
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return bin_search(arr, left, mid-1, target)
        else:
            return bin_search(arr, mid+1, right, target)
    else:
        return -1


def main():
    arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12]
    ans_1 = bin_search(arr_1, 0, len(arr_1)-1, randrange(1, len(arr_1)))
    print(f'First testcase: {ans_1} from -> {arr_1}')

    arr_random = list(range(1, randrange(1, 100)))
    ans_random = bin_search(arr=arr_random, left=0, right=len(arr_random)-1, target=randrange(1, 100))
    print(f'Random testcase: {ans_random} from -> {arr_random}')


if __name__ == '__main__':
    main()
