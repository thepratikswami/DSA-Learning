class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        reversed_num *= sign

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        return reversed_num


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().reverse(-123))
# DEBUG RUNNER END
