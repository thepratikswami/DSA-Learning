from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
# DEBUG RUNNER END
