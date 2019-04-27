# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments, key=lambda tup: tup[1])
    points = []

    for segment in segments:
        covered = False
        for point in points:
            if segment.start <= point <= segment.end:
                covered = True
        if not covered:
            points.append(segment.end)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
