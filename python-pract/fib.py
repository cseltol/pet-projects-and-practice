#fib(0) => 1
#fib(1) => 1
#fib(4) => 4
#fib(5) => 8

def fib(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)