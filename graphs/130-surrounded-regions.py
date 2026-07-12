from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Modify board in place, capturing regions not connected to a border."""
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or board[row][col] != "O"
            ):
                return

            board[row][col] = "S"  # mark border-connected as Safe
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"


# DEBUG RUNNER START
if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board)
    print(board)
# DEBUG RUNNER END
