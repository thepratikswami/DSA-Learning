class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                row[col] += row[col - 1]

        return row[-1]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))
# DEBUG RUNNER END
