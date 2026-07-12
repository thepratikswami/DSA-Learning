from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)

        return best


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# DEBUG RUNNER END
