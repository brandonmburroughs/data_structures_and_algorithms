# Uses python3

import sys


def is_greater_or_equal(a, b):
    return a + b >= b + a


def largest_number(a):
    largest_number = ""

    while a:
        max_digit = "0"
        for digit in a:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit

        largest_number += max_digit
        a.pop(a.index(max_digit))

    return largest_number


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
