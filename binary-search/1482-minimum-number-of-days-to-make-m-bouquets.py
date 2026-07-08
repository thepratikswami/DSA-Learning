from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make(day: int) -> bool:
            bouquets = 0
            consecutive = 0
            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1

        return left


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().minDays([1, 10, 3, 10, 2], 3, 1))
# DEBUG RUNNER END
