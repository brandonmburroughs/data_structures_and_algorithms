# Uses python3
def edit_distance(s, t):
    # Convert to list of characters as s and t are strings
    a = list(s)
    n = len(a)
    b = list(t)
    m = len(b)

    # Initialize edit distances matrix
    edit_distances = []
    for i in range(n + 1):
        row = []

        for j in range(m + 1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(None)

        edit_distances.append(row)

    # Create edit distance matrix
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            insertion = edit_distances[i][j - 1] + 1
            deletion = edit_distances[i - 1][j] + 1
            match = edit_distances[i - 1][j - 1]
            mismatch = edit_distances[i - 1][j - 1] + 1

            if a[i - 1] == b[j - 1]:  # index for characters is one behind matrix due to zero-indexing
                edit_distances[i][j] = min(insertion, deletion, match)
            else:
                edit_distances[i][j] = min(insertion, deletion, mismatch)

    return edit_distances[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
