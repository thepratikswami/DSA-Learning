class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If digits remain to remove, drop from the end (stack is increasing).
        if k > 0:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")
        return result if result else "0"


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().removeKdigits("1432219", 3))  # "1219"
    print(Solution().removeKdigits("10200", 1))    # "200"
    print(Solution().removeKdigits("10", 2))       # "0"
# DEBUG RUNNER END
