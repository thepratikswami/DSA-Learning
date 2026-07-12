import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        # (max elevation seen on path, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return time
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))

        return -1


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().swimInWater([[0, 2], [1, 3]]))
# DEBUG RUNNER END
