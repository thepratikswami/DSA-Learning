from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(start: int, path: List[int]) -> None:
            ans.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().subsetsWithDup([1, 2, 2]))
# DEBUG RUNNER END
