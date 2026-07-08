from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag = set()
        anti_diag = set()

        def backtrack(row: int) -> None:
            if row == n:
                ans.append(["".join(line) for line in board])
                return

            for col in range(n):
                if col in cols or row - col in diag or row + col in anti_diag:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)
                backtrack(row + 1)
                anti_diag.remove(row + col)
                diag.remove(row - col)
                cols.remove(col)
                board[row][col] = "."

        backtrack(0)
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().solveNQueens(4))
# DEBUG RUNNER END
