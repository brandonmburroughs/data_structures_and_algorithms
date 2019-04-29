# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self._size = 0

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)
        self._size = n

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def left_child(self, i):
        return 2 * i + 1  # Zero index formula

    def right_child(self, i):
        return 2 * i + 2  # Zero index formula

    def sift_down(self, i):
        min_index = i  # Track the smallest value

        # Check if the left child is smaller
        l = self.left_child(i)
        if l <= self._size - 1 and self._data[l] < self._data[min_index]:
            min_index = l

        # Check if the right child is smaller
        r = self.right_child(i)
        if r <= self._size - 1 and self._data[r] < self._data[min_index]:
            min_index = r

        # Check if we need to make an update
        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.sift_down(min_index)

    def GenerateSwaps(self):
        for i in range(self._size // 2, -1, -1):
            self.sift_down(i)

    def Solve(self, write=True):
        self.ReadData()
        self.GenerateSwaps()
        if write:
            self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
