import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []

        for start, end in intervals:
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)

        return len(rooms)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
# DEBUG RUNNER END
