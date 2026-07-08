from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            ans += counts.get(prefix - k, 0)
            counts[prefix] = counts.get(prefix, 0) + 1

        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().subarraySum([1, 1, 1], 2))
# DEBUG RUNNER END
