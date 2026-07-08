from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i, height in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > height:
                index, prev_height = stack.pop()
                best = max(best, prev_height * (i - index))
                start = index
            stack.append((start, height))

        return best


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
# DEBUG RUNNER END
