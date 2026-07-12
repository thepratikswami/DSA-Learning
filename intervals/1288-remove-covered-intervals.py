from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        count = 0
        prev_end = 0

        for _, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end

        return count


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
# DEBUG RUNNER END
