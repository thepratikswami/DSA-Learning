from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # All digits were 9, e.g. 999 -> 1000.
        return [1] + digits


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 9]))
    print(Solution().plusOne([9, 9, 9]))
# DEBUG RUNNER END
