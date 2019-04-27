# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    values_per_weights = sorted(
        [(val / weight, weight) for val, weight in zip(values, weights)],
        key=lambda tup: tup[0],
        reverse=True
    )

    for value_per_weight, weight in values_per_weights:
        if capacity == 0:
            return value

        amount = min(capacity, weight)
        value += amount * value_per_weight
        capacity -= amount

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
