from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= i ^ num

        return missing


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().missingNumber([3, 0, 1]))
# DEBUG RUNNER END
