from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for x in nums2:
            while stack and stack[-1] < x:
                next_greater[stack.pop()] = x
            stack.append(x)

        return [next_greater.get(x, -1) for x in nums1]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
# DEBUG RUNNER END
