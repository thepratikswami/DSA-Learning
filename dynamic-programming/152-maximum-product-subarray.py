from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        cur_max, cur_min = 1, 1

        for num in nums:
            cur_max, cur_min = max(num, num * cur_max, num * cur_min), min(
                num, num * cur_max, num * cur_min
            )
            result = max(result, cur_max)

        return result


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
# DEBUG RUNNER END
