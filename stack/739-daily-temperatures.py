from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)

        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# DEBUG RUNNER END
