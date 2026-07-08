from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().findMin([3, 4, 5, 1, 2]))
# DEBUG RUNNER END
