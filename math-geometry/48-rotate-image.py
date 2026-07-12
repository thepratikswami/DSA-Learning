from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate the matrix 90 degrees clockwise in place (returns None)."""
        n = len(matrix)

        # Transpose across the main diagonal.
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row.
        for row in matrix:
            row.reverse()


# DEBUG RUNNER START
if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(grid)
    print(grid)
# DEBUG RUNNER END
