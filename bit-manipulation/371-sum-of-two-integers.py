class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        a &= mask

        # If the sign bit (bit 31) is set, the result is negative in 32-bit
        # two's complement, so convert it back to a Python negative int.
        if a >> 31:
            return ~(a ^ mask)
        return a


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().getSum(2, 3))
# DEBUG RUNNER END
