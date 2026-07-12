class Solution:
    def numDecodings(self, s: str) -> int:
        prev, curr = 1, 0 if s[0] == "0" else 1

        for i in range(1, len(s)):
            nxt = 0
            if s[i] != "0":
                nxt += curr
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                nxt += prev
            prev, curr = curr, nxt

        return curr


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().numDecodings("226"))
# DEBUG RUNNER END
