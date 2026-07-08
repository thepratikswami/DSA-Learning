from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


# DEBUG RUNNER START
if __name__ == "__main__":
    first = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = second
    print(Solution().hasCycle(first))
# DEBUG RUNNER END
