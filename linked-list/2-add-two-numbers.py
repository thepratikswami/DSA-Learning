from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry, digit = divmod(total, 10)
            curr.next = ListNode(digit)
            curr = curr.next

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

    # 342 + 465 = 807 -> stored reversed as [7, 0, 8]
    l1 = build([2, 4, 3])
    l2 = build([5, 6, 4])
    print(values(Solution().addTwoNumbers(l1, l2)))
# DEBUG RUNNER END
