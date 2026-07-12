from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []

        def backtrack(index: int, path: List[str]) -> None:
            if index == len(digits):
                ans.append("".join(path))
                return

            for letter in mapping[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
# DEBUG RUNNER END
