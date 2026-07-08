from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        removed = 0
        end = float("-inf")

        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                removed += 1

        return removed


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
# DEBUG RUNNER END
