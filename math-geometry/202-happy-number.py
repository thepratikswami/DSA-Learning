class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(x: int) -> int:
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        slow = n
        fast = next_number(n)
        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return fast == 1


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().isHappy(19))
# DEBUG RUNNER END
