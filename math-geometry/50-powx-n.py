class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n

        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().myPow(2.0, 10))
    print(Solution().myPow(2.0, -2))
# DEBUG RUNNER END
