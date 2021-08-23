from typing import List


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    result = []
    mid = int(len(arr) / 2)
    y = merge_sort(arr[:mid])
    z = merge_sort(arr[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


if __name__ == '__main__':
    a = [2, 1, 4, 0, 6, 9]
    print(merge_sort(a))
