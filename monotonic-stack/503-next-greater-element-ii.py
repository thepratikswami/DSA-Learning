from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []  # holds indices, values strictly decreasing

        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                ans[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)

        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().nextGreaterElements([1, 2, 1]))
    print(Solution().nextGreaterElements([1, 2, 3, 4, 3]))
# DEBUG RUNNER END
