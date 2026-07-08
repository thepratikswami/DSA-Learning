from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

        return write


# DEBUG RUNNER START
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = Solution().removeDuplicates(nums)
    print(k, nums[:k])
# DEBUG RUNNER END
