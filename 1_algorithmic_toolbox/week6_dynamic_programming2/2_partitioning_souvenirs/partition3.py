# Uses python3
import sys
import itertools


def partition3_brute_force(A):
    # Create all ways to split len(A) elements into three groups
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            # Sum up the value for each of the three groups based upon this split
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def optimal_weight(W, w, return_weights=False):
    """From the first problem."""
    n_items = len(w)
    optimal_weights = [[0 for _ in range(W + 1)] for _ in range(n_items + 1)]

    for item_number in range(1, n_items + 1):  # Loop through number of items
        for current_weight in range(1, W + 1):  # Loop through weights
            # Get weight if we didn't add this item
            optimal_weights[item_number][current_weight] = optimal_weights[item_number - 1][current_weight]

            item_weight = w[item_number - 1]
            if item_weight <= current_weight:  # If we have the capacity for this weight
                # Get the weight for the total minus this item plus the weight of the item
                val = optimal_weights[item_number - 1][current_weight - item_weight] + item_weight

                # Update it if larger
                if val > optimal_weights[item_number][current_weight]:
                    optimal_weights[item_number][current_weight] = val

    if return_weights:
        return optimal_weights[n_items][W], optimal_weights
    else:
        return optimal_weights[n_items][W]


def reconstruct_knapsack(optimal_weights, A, capacity):
    """This took a while to figure out the edge cases!"""
    i, j = len(A), len(optimal_weights[0]) - 1
    knapsack = []

    while i + j != 0 and sum(knapsack) != capacity:
        without_item_weight = optimal_weights[i - 1][j]
        with_item_weight = optimal_weights[i - 1][j - A[i - 1]]

        if sum(knapsack) + A[i - 1] > capacity:
            i = i - 1
        else:
            if without_item_weight > with_item_weight + A[i - 1]:
                i = i - 1
            else:
                knapsack.append(A[i - 1])
                j = j - A[i - 1]
                i = i - 1

    return knapsack


def partition3(A):
    """One way to think about this problem is running knapsack without repetition three
    times.  First, we can find the capacity of each knapsack by dividing the total value
    by three.  Then, we can see if we can fill the first knapsack with exactly a weight
    of capacity.  If this works, we know there are some number of values that add up
    to our capacity.  We can reconstruct our knapsack items in order to remove them from
    the list of possible values.  Now, we want to try this again with our remaining
    values.  Since we have removed the already taken values, if the optimal weight is
    the same as the capacity, we know that these remaining values will also add up to
    the capacity.  Thus, we've found an equal split and can return 1."""
    # Check if this is possible
    if len(A) < 3:
        return 0
    total = sum(A)
    if total % 3 != 0:
        return 0

    # If it is, it's like there are three knapsacks of capacity sum(A) / 3
    capacity = total // 3
    A.sort()
    knapsack_1_weight, optimal_weights_1 = optimal_weight(capacity, A, return_weights=True)
    if knapsack_1_weight == capacity:
        knapsack_1_items = reconstruct_knapsack(optimal_weights_1, A, capacity)

        for item in knapsack_1_items:
            A.remove(item)

        knapsack_2_weight = optimal_weight(capacity, A)
        if knapsack_2_weight == capacity:
            return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
