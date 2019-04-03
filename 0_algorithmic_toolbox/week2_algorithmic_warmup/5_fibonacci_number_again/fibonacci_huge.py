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

    return fibs[-1]


def get_fibonacci_huge_fast(n, m):
    period = 0
    previous, current = 0, 1
    fibs_mod = [0 % m, 1 % m]

    for i in range(2, m * m):
        previous, current = current, current + previous
        fibs_mod.append(current % m)
        if fibs_mod[-1] == 1 and fibs_mod[-2] == 0:
            period = i - 1
            break

    return calc_fib(n % period) % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
