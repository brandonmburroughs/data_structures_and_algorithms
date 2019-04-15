#Uses python3
import sys


def matrix_max(matrix):
    """Return the max element in a 2x2 matrix."""
    return max([max(row2) for row1 in matrix for row2 in row1])


def subset_matrix(matrix, i, j, k):
    """Return the matrix of size (i, j) starting at (0, 0) in matrix."""
    return [[row2[:k] for row2 in row1[:j]] for row1 in matrix[:i]]


def lcs3_too_slow(a, b, c):  # Matrix max and matrix subset are too slow for when they are called often, e.g. identical arrays
    n = len(a)
    m = len(b)
    l = len(c)

    longest_common_subsequence_length = []
    for i in range(n + 1):
        row1 = []
        for j in range(m + 1):
            row2 = []
            for k in range(l + 1):
                row2.append(0)
            row1.append(row2)
        longest_common_subsequence_length.append(row1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    longest_common_subsequence_length[i][j][k] = matrix_max(subset_matrix(longest_common_subsequence_length, i, j, k)) + 1

    return matrix_max(longest_common_subsequence_length)


def lcs3(a, b, c):
    n = len(a)
    m = len(b)
    l = len(c)

    longest_common_subsequence_length = []
    for i in range(n + 1):
        row1 = []
        for j in range(m + 1):
            row2 = []
            for k in range(l + 1):
                row2.append(0)
            row1.append(row2)
        longest_common_subsequence_length.append(row1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    longest_common_subsequence_length[i][j][k] = longest_common_subsequence_length[i - 1][j - 1][k - 1] + 1
                else:
                    longest_common_subsequence_length[i][j][k] = max(
                        longest_common_subsequence_length[i - 1][j][k],
                        longest_common_subsequence_length[i][j - 1][k],
                        longest_common_subsequence_length[i][j][k - 1],
                        longest_common_subsequence_length[i - 1][j - 1][k],
                        longest_common_subsequence_length[i - 1][j][k - 1],
                        longest_common_subsequence_length[i][j - 1][k - 1],
                    )

    return longest_common_subsequence_length[n][m][l]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
