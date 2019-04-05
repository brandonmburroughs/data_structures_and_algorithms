# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):
    mod = 10
    period = 60
    previous, current = 0, 1

    for i in range(2, n % period + 2):
        previous, current = current % mod, (current + previous) % mod

    return (current * previous) % mod


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
