from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            ans[i] = prefix
            prefix *= num

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
# DEBUG RUNNER END
