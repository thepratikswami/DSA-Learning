from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int, path: List[str]) -> None:
            if start == len(s):
                ans.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().partition("aab"))
# DEBUG RUNNER END
