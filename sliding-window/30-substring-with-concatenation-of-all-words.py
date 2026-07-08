from typing import List
from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target = Counter(words)
        ans = []

        for offset in range(len(words[0])):
            print(f"Offset: {offset}")
            left = offset
            right = offset
            window = defaultdict(int)

            while right + len(words[0]) <= len(s):
                word = s[right:right + len(words[0])]
                right += len(words[0])

                if word in target:
                    window[word] += 1

                    while window[word] > target[word]:
                        window[s[left:left + len(words[0])]] -= 1
                        left += len(words[0])

                    if right - left == len(words) * len(words[0]):
                        ans.append(left)
                else:
                    window.clear()
                    left = right
        return ans


def main():
    solution = Solution()
    result = solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(result)


if __name__ == "__main__":
    main()
