from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        possible = {0}

        for num in nums:
            possible |= {value + num for value in possible if value + num <= target}
            if target in possible:
                return True

        return False


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().canPartition([1, 5, 11, 5]))
# DEBUG RUNNER END
