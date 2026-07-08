from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            used_days = 1
            current = 0
            for weight in weights:
                if current + weight > capacity:
                    used_days += 1
                    current = 0
                current += weight
            return used_days <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# DEBUG RUNNER END
