# python3
import sys


class DisjointSet:
    def __init__(self, n_tables, rows):
        self.n_tables = n_tables
        self.rows = rows
        self.rank = [1] * n_tables
        self.parent = list(range(0, n_tables))
        self.max_rows = max(self.rows)

    def get_max_rows(self):
        return self.max_rows

    def get_parent(self, table):
        # Find parent and compress path
        if table != self.parent[table]:
            self.parent[table] = self.get_parent(self.parent[table])

        return self.parent[table]

    def merge(self, destination, source):
        destination_parent, source_parent = self.get_parent(destination), self.get_parent(source)

        # The tables are already merged
        if destination_parent == source_parent:
            return

        # Merge two tables with union by rank heuristic
        if self.rank[destination_parent] > self.rank[source_parent]:
            self.parent[source_parent] = destination_parent
            # Add rows
            self.rows[destination_parent] += self.rows[source_parent]
            self.rows[source_parent] = 0
            # Update max
            self.max_rows = max(self.max_rows, self.rows[destination_parent])
        else:
            self.parent[destination_parent] = source_parent
            # Add rows
            self.rows[source_parent] += self.rows[destination_parent]
            self.rows[destination_parent] = 0
            # Update max
            self.max_rows = max(self.max_rows, self.rows[source_parent])

            # If the ranks were equal, we need to update them
            if self.rank[destination_parent] == self.rank[source_parent]:
                self.rank[source_parent] += 1


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    disjoint_set = DisjointSet(n, lines)

    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        disjoint_set.merge(destination - 1, source - 1)
        print(disjoint_set.get_max_rows())
