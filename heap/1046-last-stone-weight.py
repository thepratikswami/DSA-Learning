import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
# DEBUG RUNNER END
