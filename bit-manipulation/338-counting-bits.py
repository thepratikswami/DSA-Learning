from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)

        return bits


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().countBits(5))
# DEBUG RUNNER END
