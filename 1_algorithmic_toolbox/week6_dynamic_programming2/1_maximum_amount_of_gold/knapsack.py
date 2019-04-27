# Uses python3
import sys


def optimal_weight(W, w):
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

    return optimal_weights[n_items][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
