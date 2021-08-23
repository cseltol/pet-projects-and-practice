import time
from functools import lru_cache
from matplotlib import pyplot as plt


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], lable=f.__name__)
    plt.legend()
    plt.grid(True)


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def fib(n):
    assert n >= 0
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=3)
def fib_recursive(n):
    assert n >= 0
    return n if n <= 1 else fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def main():
    assert fib_recursive(8) == 21
    # print(timed(fib_recursive, 8))

    assert fib_iterative(8) == 21
    # print(timed(fib_iterative, 8))
    # print(timed(fib_iterative, 80))
    # print(timed(fib_iterative, 800))
    # print(timed(fib_iterative, 8000))

    print(compare([fib, fib_iterative], list(range(20))))


if __name__ == '__main__':
    main()
