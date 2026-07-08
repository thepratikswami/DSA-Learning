from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)
        ans.extend(intervals[i:])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
# DEBUG RUNNER END
