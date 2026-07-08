from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        target = Counter(t)
        ans = float("inf")

        for right, value in enumerate(s):

            if value in target:
                target[value] -= 1

            while all(count <= 0 for count in target.values()):
                if right - left + 1 < ans:
                    ans = right - left + 1
                    start = left

                if s[left] in target:
                    target[s[left]] += 1
                left += 1
                
        return s[start:start + ans] if ans != float("inf") else ""


def main():
    solution = Solution()
    result = solution.minWindow("ADOBECODEBANC", "ABC")
    print(result)


if __name__ == "__main__":
    main()
