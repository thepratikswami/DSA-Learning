from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


# DEBUG RUNNER START
if __name__ == "__main__":
    def build(values):
        dummy = ListNode()
        curr = dummy
        for value in values:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next

    def values(head):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    print(values(Solution().removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))
# DEBUG RUNNER END
