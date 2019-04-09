# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    # Put all points in one large array that can be sorted
    all_points = starts + ends + points
    # Sort by point value and then lexical to get l, p, r order if tied
    all_points = sorted(all_points, key=lambda tup: (tup[0], tup[1]))

    l, r = 0, 0
    for point, point_type in all_points:
        if point_type == "l":
            l += 1
        elif point_type == "r":
            r += 1
        else:
            cnt[points.index((point, point_type))] += l - r

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = []
    ends = []
    for i in range(2, 2 * n + 2, 2):
        starts.append((data[i], "l"))
    for i in range(3, 2 * n + 2, 2):
        ends.append((data[i], "r"))

    points = []
    for i in range(2 * n + 2, len(data)):
        points.append((data[i], "p"))

    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
