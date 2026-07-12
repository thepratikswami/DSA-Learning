from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(open_count: int, close_count: int) -> None:
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
# DEBUG RUNNER END
