from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
# DEBUG RUNNER END
