# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):
    m = 10
    if n in [0, 1]:
        return n % m
    period = 60

    previous, current = 0, 1
    fib_mod_sum = 1

    fibs_range = (period if n % period == 0 else n % period) + 1
    for i in range(2, fibs_range):
        previous, current = current % m, (current + previous) % m
        fib_mod_sum += current
        fib_mod_sum = fib_mod_sum % m

    return fib_mod_sum


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
