from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
# DEBUG RUNNER END
