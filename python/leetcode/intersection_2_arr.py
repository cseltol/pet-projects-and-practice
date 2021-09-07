import collections


def intersect(nums1, nums2):
    a = []
    m = dict(collections.Counter(nums1))

    for i in nums2:
        if i in m:
            if m[i] > 0:
                a.append(i)
                m[i] -= 1
    return a


def main():
    print(intersect([1, 2, 2, 1], [2, 2]))


if __name__ == '__main__':
    main()
