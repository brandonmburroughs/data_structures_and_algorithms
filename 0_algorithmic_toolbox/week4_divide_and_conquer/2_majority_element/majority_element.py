# Uses python3
import sys


def get_majority_element_brute_force(a):
    for i in range(len(a)):
        count = 0

        for j in range(len(a)):
            if a[i] == a[j]:
                count += 1

        if count > n / 2:
            return a[i]

    return -1


def get_majority_element(a, left, right):
    # If the list is empty
    if left == right:
        return -1
    # If the list is of length 1
    if left + 1 == right:
        return a[left]

    # Divide into two subproblems
    mid = left + (right - left) // 2

    # Get majority element for each subproblem
    majority_element_left = get_majority_element(a, left, mid)
    majority_element_right = get_majority_element(a, mid, right)

    # If the left and right majority element are the same
    if majority_element_left == majority_element_right:
        return majority_element_left

    # Loop through array and check if they match
    count_left, count_right = 0, 0
    for element in a[left:right]:
        if element == majority_element_left:
            count_left += 1
        if element == majority_element_right:
            count_right += 1

    # Check for over half
    if count_left > (right - left) // 2:
        return majority_element_left
    if count_right > (right - left) // 2:
        return majority_element_right

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
    #if get_majority_element_brute_force(a) != 1:
        print(1)
    else:
        print(0)
