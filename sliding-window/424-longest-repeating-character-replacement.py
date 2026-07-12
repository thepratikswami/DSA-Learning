from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        max_freq = 0
        best = 0

        for right, char in enumerate(s):
            counts[char] += 1
            max_freq = max(max_freq, counts[char])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().characterReplacement("AABABBA", 1))
# DEBUG RUNNER END
