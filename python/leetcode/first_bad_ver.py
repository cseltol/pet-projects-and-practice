def isBadVersion(n):
    return True if n % 2 == 0 else False


def firstBadVersion(n):
        mid = 0
        low = 1
        high = n
        result = n
        
        while low <= high:
            mid = int((low + high) / 2)
            if isBadVersion(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        

if __name__ == '__main__':
    vers = [1, 2, 3, 4, 5]
    for i in range(len(vers)):
        print(firstBadVersion(vers[i]))
