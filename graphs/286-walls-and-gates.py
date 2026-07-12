from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """Fill each empty room in place with the distance to its nearest gate."""
        if not rooms or not rooms[0]:
            return

        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == INF:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r, c))


# DEBUG RUNNER START
if __name__ == "__main__":
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    Solution().wallsAndGates(rooms)
    print(rooms)
# DEBUG RUNNER END
