class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = []

        for i, c in enumerate(s):
            if c in seen:
                continue
            # Pop bigger characters that still appear later, keeping order small.
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                seen.discard(stack.pop())
            stack.append(c)
            seen.add(c)

        return "".join(stack)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().removeDuplicateLetters("bcabc"))     # "abc"
    print(Solution().removeDuplicateLetters("cbacdcbc"))  # "acdb"
# DEBUG RUNNER END
