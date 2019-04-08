# Uses python3
import sys
import random


def partition3_lomuto(a, l, r):
    pivot = a[l]  # Pivot
    equal_idx = l  # Equal elements end index
    less_idx = l  # Less than element end index

    for current_idx in range(l + 1, r + 1):
        if a[current_idx] < pivot:
            less_idx += 1
            a[less_idx], a[current_idx] = a[current_idx], a[less_idx]
        elif a[current_idx] == pivot:
            less_idx += 1
            equal_idx += 1

            # Put the current value at the end of the equals
            a[equal_idx], a[current_idx] = a[current_idx], a[equal_idx]

            # If there are actually less thans
            if less_idx > equal_idx:
                # The less than just got moved to the current position; move it back
                a[less_idx], a[current_idx] = a[current_idx], a[less_idx]

    # Swap equals and less thans
    equal_pos = l  # Start at where the equals begin
    for i in range(equal_idx + 1, less_idx + 1):
        a[equal_pos], a[i] = a[i], a[equal_pos]
        equal_pos += 1
    return less_idx, less_idx - (equal_idx - l)


def partition3(a, l, r):
    """Hoare's partition:  https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme"""
    pivot = a[l]
    low = l
    high = r
    i = l

    while i <= high:
        # Move low points to the front
        if a[i] < pivot:
            a[i], a[low] = a[low], a[i]
            low += 1
            i += 1
        # Move high points to the end
        elif a[i] > pivot:
            a[i], a[high] = a[high], a[i]
            high -= 1
        else:
            i += 1

    return low, high


def partition2(a, l, r):
    x = a[l]  # Get pivot element
    j = l  # Set endpoint of values less than pivot to the beginning
    for i in range(l + 1, r + 1):  # Loop through all values
        if a[i] <= x:  # If the point is less than the pivot
            j += 1  # Move the endpoint up one
            a[i], a[j] = a[j], a[i]  # Put that element at the end of the less thans
    a[l], a[j] = a[j], a[l]  # Swap pivot and end of less thans
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]  # In place swap
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
