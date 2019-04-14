# Uses python3
import sys


def get_change(money):
    coins = [1, 3, 4]
    min_num_coins = [0] + [sys.maxsize] * money

    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1

                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]


if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
