# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    fibs = [0, 1]

    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return int(str(fibs[-1])[-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(n)
    print(get_fibonacci_last_digit_fast(n))
