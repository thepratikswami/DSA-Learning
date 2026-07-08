from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_prev = skip_prev = 0

        for num in nums:
            rob_prev, skip_prev = skip_prev + num, max(rob_prev, skip_prev)

        return max(rob_prev, skip_prev)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))
# DEBUG RUNNER END
