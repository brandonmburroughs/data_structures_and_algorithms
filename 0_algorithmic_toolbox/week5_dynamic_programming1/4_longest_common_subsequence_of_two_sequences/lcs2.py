#Uses python3
import sys


def matrix_max(matrix):
    """Return the max element in a 2x2 matrix."""
    return max([max(row) for row in matrix])


def subset_matrix(matrix, i, j):
    """Return the matrix of size (i, j) starting at (0, 0) in matrix."""
    return [row[:j] for row in matrix[:i]]


def lcs2(a, b):
    n = len(a)
    m = len(b)

    longest_common_subsequence_lengths = []
    for i in range(n + 1):
        row = []
        for j in range(m + 1):
            row.append(0)
        longest_common_subsequence_lengths.append(row)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                longest_common_subsequence_lengths[i][j] = matrix_max(subset_matrix(longest_common_subsequence_lengths, i, j)) + 1

    return matrix_max(longest_common_subsequence_lengths)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
