# Uses python3
import sys


def get_change(m):
    n_coins = 0
    coins = [10, 5, 1]

    for coin in coins:
        while m >= coin:
            n_coins += 1
            m -= coin

    return n_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
