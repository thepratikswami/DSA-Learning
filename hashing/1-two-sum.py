from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i

        return []


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
# DEBUG RUNNER END
