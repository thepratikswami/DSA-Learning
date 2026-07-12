from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or board[r][c] != word[index]
            ):
                return False

            board[r][c] = "#"
            found = (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )
            board[r][c] = word[index]
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False


# DEBUG RUNNER START
if __name__ == "__main__":
    grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print(Solution().exist(grid, "ABCCED"))
# DEBUG RUNNER END
