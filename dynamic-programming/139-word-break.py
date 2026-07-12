from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if dp[j] and s[i:j] in words:
                    dp[i] = True
                    break

        return dp[0]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))
# DEBUG RUNNER END
