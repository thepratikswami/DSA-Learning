from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remaining:
                    break
                path.append(candidate)
                backtrack(i, remaining - candidate, path)
                path.pop()

        backtrack(0, target, [])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
# DEBUG RUNNER END
