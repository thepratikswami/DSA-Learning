import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# DEBUG RUNNER START
if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print([kth.add(3), kth.add(5), kth.add(10), kth.add(9), kth.add(4)])
# DEBUG RUNNER END
