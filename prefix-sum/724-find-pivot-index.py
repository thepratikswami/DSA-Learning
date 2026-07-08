from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num

        return -1


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
# DEBUG RUNNER END
