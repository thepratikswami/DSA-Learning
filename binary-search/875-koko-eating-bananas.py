from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
# DEBUG RUNNER END
