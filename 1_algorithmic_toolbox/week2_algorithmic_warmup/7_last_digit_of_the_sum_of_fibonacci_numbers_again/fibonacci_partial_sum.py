# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_fast(from_, to):
    # Edge cases
    if to == 0:
        return 0
    if to == 1:
        return 1

    # Initialize all the things
    mod = 10
    period = 60  # period_sum_mod = 0, so it doesn't affect last digit
    previous, current = 0, 1
    fib_sum_mod = 0

    # Iterate through from_ up to the end of a period
    from_mod = from_ % period
    to_reset = to - from_ // period * period

    # Case when we start at from <= 1
    if from_mod <= 1:
        fib_sum_mod += 1

    for i in range(2, period + 1):
        previous, current = current % mod, (current + previous) % mod

        if from_mod <= i <= to_reset:
            fib_sum_mod += current
            fib_sum_mod %= mod

    if to_reset <= period:
        return fib_sum_mod

    n_periods = to // period - 1

    previous, current = 0, 1
    fib_sum_mod += 1
    for i in range(2, to - (n_periods + 1) * period + 1):
        previous, current = current % mod, (current + previous) % mod
        fib_sum_mod += current
        fib_sum_mod %= mod

    return fib_sum_mod


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
