# Uses python3
def calc_fib(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[-1]


n = int(input())
print(calc_fib(n))
