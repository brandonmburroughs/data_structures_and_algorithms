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
    previous, current = 0, 1
    period = 60
    fib_sum_mod = 0
    period_sum = 1

    # Case when we start at from <= 1
    if from_ <= 1:
        fib_sum_mod += 1

    # Iterate through a period's worth of values
    for i in range(2, period + 1):
        # Calculate fib numbers
        previous, current = current % mod, (current + previous) % mod

        # All values get added to period sum
        period_sum += current
        period_sum %= mod

        # Only add these values if i is in the from - to range
        if from_ <= i <= to:
            fib_sum_mod += current
            fib_sum_mod %= mod

    if to <= period:
        return fib_sum_mod

    n_periods = (to - from_) // period - 1
    n_periods = 0 if n_periods < 0 else n_periods
    fib_sum_mod += n_periods * period_sum
    fib_sum_mod %= mod

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
