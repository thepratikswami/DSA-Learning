from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# DEBUG RUNNER END
