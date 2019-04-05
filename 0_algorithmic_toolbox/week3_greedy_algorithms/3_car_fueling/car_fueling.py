# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_stop = 0
    stops.insert(0, 0)
    stops.append(distance)

    while stops[current_stop] < distance:
        last_stop = current_stop
        while stops[current_stop] < distance and stops[current_stop + 1] - stops[last_stop] <= tank:
            current_stop += 1
        if current_stop == last_stop:  # Haven't gone anywhere
            return -1
        if stops[current_stop] < distance:
            num_refills += 1

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
