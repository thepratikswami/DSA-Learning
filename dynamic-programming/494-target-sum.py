from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = {0: 1}

        for num in nums:
            nxt = defaultdict(int)
            for total, ways in counts.items():
                nxt[total + num] += ways
                nxt[total - num] += ways
            counts = nxt

        return counts.get(target, 0)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
# DEBUG RUNNER END
