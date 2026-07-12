from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))
            minutes += 1

        return minutes if fresh == 0 else -1


# DEBUG RUNNER START
if __name__ == "__main__":
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    print(Solution().orangesRotting(grid))
# DEBUG RUNNER END
