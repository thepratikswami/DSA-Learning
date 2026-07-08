class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = []
        number = 0

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == "[":
                stack.append(("".join(current), number))
                current = []
                number = 0
            elif char == "]":
                previous, repeat = stack.pop()
                current = [previous + "".join(current) * repeat]
            else:
                current.append(char)

        return "".join(current)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().decodeString("3[a2[c]]"))
# DEBUG RUNNER END
