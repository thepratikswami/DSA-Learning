class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            best = max(best, right - left + 1)

        return best


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
# DEBUG RUNNER END
