from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


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

    print(values(Solution().reverseList(build([1, 2, 3, 4, 5]))))
# DEBUG RUNNER END
