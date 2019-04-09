# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    if len(starts) == 1:
        for i, point in enumerate(points):
            if starts[0] <= point <= ends[0]:
                cnt[i] += 1

        return cnt

    mid = len(starts) // 2
    left_cnt = fast_count_segments(starts[mid:], ends[mid:], points)
    right_cnt = fast_count_segments(starts[:mid], ends[:mid], points)

    for i in range(len(left_cnt)):
        cnt[i] = left_cnt[i] + right_cnt[i]

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
