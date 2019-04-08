# Uses python3
import sys


def get_number_of_inversions_brute_force(a):
    number_of_inversions = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                number_of_inversions += 1

    return number_of_inversions


def merge(b, c):
    number_of_inversions_across_merge = 0
    merged_list = []

    i, j = 0, 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            merged_list.append(b[i])
            i += 1
        else:
            number_of_inversions_across_merge += len(b[i:])
            merged_list.append(c[j])
            j += 1

    # Add the remaining elements to the list
    merged_list.extend(b[i:])
    merged_list.extend(c[j:])

    return merged_list, number_of_inversions_across_merge


def get_number_of_inversions(a, number_of_inversions=0):
    if len(a) == 1:
        return a, number_of_inversions
    mid = len(a) // 2
    left_sorted, number_of_inversions_left = get_number_of_inversions(a[:mid])
    right_sorted, number_of_inversions_right = get_number_of_inversions(a[mid:])

    a_sorted, number_of_inversions_across_merge = merge(left_sorted, right_sorted)
    number_of_inversions = number_of_inversions_left + number_of_inversions_right + number_of_inversions_across_merge

    return a_sorted, number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a_sorted, number_of_inversions = get_number_of_inversions(a)
    print(number_of_inversions)
