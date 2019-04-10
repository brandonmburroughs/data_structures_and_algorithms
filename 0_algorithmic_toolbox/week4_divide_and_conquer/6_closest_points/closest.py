#Uses python3
import sys
import math
import datetime


def compute_distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def minimum_distance_brute_force(x, y):
    min_distance = sys.maxsize

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            distance = compute_distance(x[i], x[j], y[i], y[j])
            if distance < min_distance:
                min_distance = distance

    return min_distance


def minimum_distance_too_slow(x, y):
    # Handle base cases for small groups of points
    if len(x) == 1:
        return sys.maxsize
    if len(x) == 2:
        return compute_distance(x[0], x[1], y[0], y[1])
    elif len(x) == 3:
        return min(
            compute_distance(x[0], x[1], y[0], y[1]),
            compute_distance(x[0], x[2], y[0], y[2]),
            compute_distance(x[1], x[2], y[1], y[2])
        )

    # Get x coordinate that splits data into two equal sets
    if len(x) % 2 == 0:
        mid_x = sum(
            sorted(x)[(len(x) // 2 - 1):(len(x) // 2 + 1)]
        ) / 2
    else:
        mid_x = sorted(x)[len(x) // 2]

    # Create the two separate, equal sets
    s1_x, s1_y, s2_x, s2_y = [], [], [], []
    for i in range(len(x)):
        if x[i] <= mid_x:
            s1_x.append(x[i])
            s1_y.append(y[i])
        else:
            s2_x.append(x[i])
            s2_y.append(y[i])

    if len(s1_x) == len(x):
        idx = s1_x.index(mid_x)
        s2_x.append(s1_x.pop(idx))
        s2_y.append(s1_y.pop(idx))
    elif len(s2_x) == len(x):
        idx = s2_x.index(mid_x)
        s1_x.append(s2_x.pop(idx))
        s1_y.append(s2_y.pop(idx))

    # Divide into subproblems
    min_distance_left = minimum_distance_too_slow(s1_x, s1_y)
    min_distance_right = minimum_distance_too_slow(s2_x, s2_y)
    min_distance = min(min_distance_left, min_distance_right)

    # Check min distance for points that are in either set
    filtered_points_in_strip = []
    for i in range(len(x)):
        if math.fabs(x[i] - mid_x) < min_distance:
            filtered_points_in_strip.append((x[i], y[i]))

    filtered_points_in_strip = sorted(filtered_points_in_strip, key=lambda tup: tup[1])

    for i in range(0, len(filtered_points_in_strip)):
        for j in range(i + 1, min(len(filtered_points_in_strip), i + 7)):
            x2, y2 = filtered_points_in_strip[j]
            x1, y1 = filtered_points_in_strip[i]
            dist = compute_distance(x1, x2, y1, y2)
            if dist < min_distance:
                min_distance = dist

    return min_distance


def minimum_distance_sorted(x, y):
    n_x = len(x)

    # Handle base cases for small groups of points
    if n_x == 1:
        return sys.maxsize
    if n_x == 2:
        return compute_distance(x[0][0], x[1][0], x[0][1], x[1][1])
    elif n_x == 3:
        return min(
            compute_distance(x[0][0], x[1][0], x[0][1], x[1][1]),
            compute_distance(x[0][0], x[2][0], x[0][1], x[2][1]),
            compute_distance(x[1][0], x[2][0], x[1][1], x[2][1]),
        )

    # Get x coordinate that splits data into two equal sets
    mid = n_x // 2
    mid_x = x[mid][0]
    s1_x = x[:mid]
    s2_x = x[mid:]
    s1_x_set = set(s1_x)

    # Get corresponding y coordinates
    s1_y, s2_y = [], []
    for y_pair in y:
        if y_pair in s1_x_set:
            s1_y.append(y_pair)
        else:
            s2_y.append(y_pair)

    # Divide into subproblems
    min_distance_left = minimum_distance_sorted(s1_x, s1_y)
    min_distance_right = minimum_distance_sorted(s2_x, s2_y)
    min_distance = min(min_distance_left, min_distance_right)

    # Check min distance for points that are in either set
    filtered_points_in_strip = []
    for y_pair in y:
        if math.fabs(y_pair[0] - mid_x) < min_distance:
            filtered_points_in_strip.append(y_pair)

    # Check point in center strip
    n_strip = len(filtered_points_in_strip)
    for i in range(n_strip):
        for j in range(i + 1, min(n_strip, i + 7)):
            x2, y2 = filtered_points_in_strip[j]
            x1, y1 = filtered_points_in_strip[i]
            dist = compute_distance(x1, x2, y1, y2)
            if dist < min_distance:
                min_distance = dist

    return min_distance


def minimum_distance(x, y):
    points = list(zip(x, y))
    sorted_x_points = sorted(points, key=lambda tup: tup[0])
    sorted_y_points = sorted(points, key=lambda tup: tup[1])

    return minimum_distance_sorted(sorted_x_points, sorted_y_points)


if __name__ == '__main__':
    import random

    i = 0

    while True:
        n = random.randint(2, 6)
        x = [random.randint(-10, 10) for _ in range(n)]
        y = [random.randint(-10, 10) for _ in range(n)]

        try:
            min_distance = minimum_distance(x, y)
        except:
            print(f"Recursion error for n = {n}, x = {x}, y = {y}")
            break

        min_distance_brute_force = minimum_distance_brute_force(x, y)

        try:
            assert min_distance == min_distance_brute_force
        except:
            print(f"Error at n = {n}, x = {x}, y = {y}, min_distnace = {min_distance}, min_distance_brute_force = {min_distance_brute_force}")
            break

        i += 1

        if i % 10000 == 0:
            print(f"{i} successful runs!")
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    """
