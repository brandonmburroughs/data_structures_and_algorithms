# Uses python3
import sys


def optimal_summands(n):
    summands = []

    i = 1
    while i <= n:
        summands.append(i)
        n -= i
        i += 1

    if n > 0:
        summands[-1] += n

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
