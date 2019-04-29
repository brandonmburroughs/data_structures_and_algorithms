# python3
from collections import deque
import sys
import threading


def compute_height_slow(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def build_tree(parents):
    root_idx = -1
    n = len(parents)
    tree = {i: [] for i in range(n)}
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)
        else:
            root_idx = i

    return root_idx, tree


def compute_height(n, parents):
    # Base case of empty tree
    if len(parents) == 0:
        return 0

    # Build tree
    root_idx, tree = build_tree(parents)

    # BFS of tree
    max_depth = 1
    node_queue = deque()
    node_queue.append((root_idx, 1))

    while len(node_queue) > 0:
        node_idx, depth = node_queue.pop()
        if tree[node_idx]:
            depth += 1
            max_depth = max(max_depth, depth)
            for node in tree[node_idx]:
                node_queue.append((node, depth))

    return max_depth


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
