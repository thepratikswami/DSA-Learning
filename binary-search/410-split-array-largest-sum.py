from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit: int) -> bool:
            parts = 1
            current = 0
            for num in nums:
                if current + num > limit:
                    parts += 1
                    current = 0
                current += num
            return parts <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().splitArray([7, 2, 5, 10, 8], 2))
# DEBUG RUNNER END
