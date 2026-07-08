from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_at_least(value: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < value:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = first_at_least(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = first_at_least(target + 1) - 1
        return [start, end]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
# DEBUG RUNNER END
