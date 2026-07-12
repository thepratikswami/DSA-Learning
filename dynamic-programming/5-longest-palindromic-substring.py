class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, longest = 0, 0

        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > longest:
                        start, longest = left, right - left + 1
                    left -= 1
                    right += 1

        return s[start : start + longest]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
# DEBUG RUNNER END
