from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start: int, path: List[int]) -> None:
            ans.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
# DEBUG RUNNER END
