class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result |= bit << (31 - i)
        return result


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().reverseBits(0b00000010100101000001111010011100))
# DEBUG RUNNER END
