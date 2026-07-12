import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, point index)
        total = 0
        used = 0

        while used < n:
            cost, i = heapq.heappop(min_heap)
            if visited[i]:
                continue
            visited[i] = True
            total += cost
            used += 1

            xi, yi = points[i]
            for j in range(n):
                if not visited[j]:
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (dist, j))

        return total


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
# DEBUG RUNNER END
