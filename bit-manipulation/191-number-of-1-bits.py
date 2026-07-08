class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().hammingWeight(11))
# DEBUG RUNNER END
