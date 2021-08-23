import functools


def memoize(f):
    cache = {}

    @functools.wraps(f)
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]
    return inner


@memoize
def fib(n):
    assert n >= 0
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


def main():
    pass


if __name__ == '__main__':
    main()
