from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)

        return True


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
# DEBUG RUNNER END
