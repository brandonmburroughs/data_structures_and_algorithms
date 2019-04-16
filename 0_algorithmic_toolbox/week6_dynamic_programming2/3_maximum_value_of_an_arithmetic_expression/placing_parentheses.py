# Uses python3
import sys


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_min_and_max(i, j, mins, maxes, expression):
    global_min = sys.maxsize
    global_max = -sys.maxsize

    for k in range(i, j):
        op = expression[k * 2 + 1]
        a = evalt(maxes[i][k], maxes[k + 1][j], op)
        b = evalt(maxes[i][k], mins[k + 1][j], op)
        c = evalt(mins[i][k], maxes[k + 1][j], op)
        d = evalt(mins[i][k], mins[k + 1][j], op)

        global_min = min(global_min, a, b, c, d)
        global_max = max(global_max, a, b, c, d)

    return global_min, global_max


def try_convert_int(val):
    try:
        return int(val)
    except ValueError:
        return val


def get_maximum_value(dataset):
    expression = [try_convert_int(val) for val in dataset]
    n = len(expression) // 2 + 1
    mins = [[None for _ in range(n)] for _ in range(n)]
    maxes = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mins[i][i] = expression[i * 2]
        maxes[i][i] = expression[i * 2]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            mins[i][j], maxes[i][j] = get_min_and_max(i, j, mins, maxes, expression)

    return maxes[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
