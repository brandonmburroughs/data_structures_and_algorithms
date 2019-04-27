# Uses python3
import sys


def optimal_sequence_wrong(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(n):
    optimal_sequences = [[], [1]] # [list(range(1, i + 1)) for i in range(n + 1)]

    for i in range(2, n + 1):
        for previous_move in [i / 3, i / 2, i - 1]:
            if int(previous_move) == previous_move:
                previous_move = int(previous_move)

                if len(optimal_sequences) < i + 1:
                    optimal_sequences.append(optimal_sequences[previous_move] + [i])
                elif len(optimal_sequences[previous_move]) + 1 < len(optimal_sequences[i]):
                    optimal_sequences[i] = optimal_sequences[previous_move] + [i]
                    break


    return optimal_sequences[n]



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
