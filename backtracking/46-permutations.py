from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def backtrack(path: List[int]) -> None:
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
# DEBUG RUNNER END
