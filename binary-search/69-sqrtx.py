class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().mySqrt(8))
# DEBUG RUNNER END
