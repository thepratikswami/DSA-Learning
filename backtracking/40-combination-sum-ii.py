from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                candidate = candidates[i]
                if candidate > remaining:
                    break
                path.append(candidate)
                backtrack(i + 1, remaining - candidate, path)
                path.pop()

        backtrack(0, target, [])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# DEBUG RUNNER END
