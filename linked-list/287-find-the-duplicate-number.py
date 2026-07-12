from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))
# DEBUG RUNNER END
