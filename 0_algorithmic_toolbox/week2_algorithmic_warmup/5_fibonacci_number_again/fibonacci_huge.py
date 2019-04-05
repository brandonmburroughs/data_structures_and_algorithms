# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def calc_fib(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[n]


def get_fibonacci_huge_fast(n, m):
    if n in [0, 1]:
        return n % m
    period = None
    previous, current = 0, 1

    for i in range(2, m * m + 1):
        previous, current = current % m, (current + previous) % m
        if current == 1 and previous == 0:
            period = i - 1
            break

    return calc_fib(n % period) % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
