from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._rob_line(nums[1:]), self._rob_line(nums[:-1]))

    def _rob_line(self, nums: List[int]) -> int:
        rob_prev, skip_prev = 0, 0

        for num in nums:
            rob_prev, skip_prev = skip_prev + num, max(rob_prev, skip_prev)

        return max(rob_prev, skip_prev)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().rob([2, 3, 2]))
# DEBUG RUNNER END
