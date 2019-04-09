# Uses python3
import sys
import collections


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    points_map = collections.defaultdict(set)

    # Put all points in one large array that can be sorted
    all_points = []
    for start in starts:
        all_points.append((start, 'l'))
    for end in ends:
        all_points.append((end, 'r'))
    for i, point in enumerate(points):
        new_point = (point, 'p')
        if new_point not in all_points:
            all_points.append((point, 'p'))
        points_map[point].add(i)
    # Sort by point value and then lexical to get l, p, r order if tied
    all_points = sorted(all_points, key=lambda tup: (tup[0], tup[1]))

    l, r = 0, 0
    for point, point_type in all_points:
        if point_type == "l":
            l += 1
        elif point_type == "r":
            r += 1
        elif point_type == "p":
            for i in points_map[point]:
                cnt[i] += l - r

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
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
