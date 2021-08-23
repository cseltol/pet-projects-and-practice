class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        if n in self.memo:
            return self.memo[n]
        else:
            f = self.fib(n - 1) + self.fib(n - 2)

        self.memo[n] = f

        return f

input = int(input())
s = Solution()
print(f"fib({input})={s.fib(input)}")
