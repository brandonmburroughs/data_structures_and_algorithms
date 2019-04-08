# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]  # Get pivot
    j = l  # Set end of values less than pivot
    k = l  # Set end of values equal to pivot

    for i in range(l + 1, r + 1):
        if a[i] == x:  # If it's equal to the pivot
            j += 1
            k += 1
            # Swap the current element and the equal to
            a[k], a[i] = a[i], a[k]

            # Swap the current element and the less than to get it back in place
            if j > k:
                a[j], a[i] = a[i], a[j]
        elif a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i] # Swap the less than value and current value

    # Swap the less thans and equal tos
    equals_idx = 0
    for i in range(k + 1, j + 1):
        a[equals_idx], a[i] = a[i], a[equals_idx]
        equals_idx += 1

    return j - k, j + 1


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
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
