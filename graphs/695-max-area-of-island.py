from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> int:
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or grid[row][col] == 0
            ):
                return 0

            grid[row][col] = 0
            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        best = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    best = max(best, dfs(row, col))

        return best


# DEBUG RUNNER START
if __name__ == "__main__":
    grid = [[0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().maxAreaOfIsland(grid))
# DEBUG RUNNER END
