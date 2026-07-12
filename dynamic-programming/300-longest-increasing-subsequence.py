from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []

        for num in nums:
            i = bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num

        return len(tails)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# DEBUG RUNNER END
