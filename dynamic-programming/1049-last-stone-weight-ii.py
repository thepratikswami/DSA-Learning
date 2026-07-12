from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for s in range(target, stone - 1, -1):
                dp[s] = dp[s] or dp[s - stone]

        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s

        return 0


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))
# DEBUG RUNNER END
