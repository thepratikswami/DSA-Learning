from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row: int, col: int, reachable: set, prev_height: int) -> None:
            if (
                (row, col) in reachable
                or row < 0
                or row == rows
                or col < 0
                or col == cols
                or heights[row][col] < prev_height
            ):
                return

            reachable.add((row, col))
            height = heights[row][col]
            dfs(row + 1, col, reachable, height)
            dfs(row - 1, col, reachable, height)
            dfs(row, col + 1, reachable, height)
            dfs(row, col - 1, reachable, height)

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        return [[row, col] for row, col in pacific & atlantic]


# DEBUG RUNNER START
if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(sorted(Solution().pacificAtlantic(heights)))
# DEBUG RUNNER END
