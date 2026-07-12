import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().kClosest([[1, 3], [-2, 2]], 1))
# DEBUG RUNNER END
