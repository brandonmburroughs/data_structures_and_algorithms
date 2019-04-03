# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    max_number = -1
    max_number_2 = -1

    for number in numbers:
        if number > max_number:
            max_number_2 = max_number
            max_number = number
        elif number > max_number_2:
            max_number_2 = number

    return max_number * max_number_2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
