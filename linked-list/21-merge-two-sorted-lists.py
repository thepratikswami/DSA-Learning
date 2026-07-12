from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
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

    l1 = build([1, 2, 4])
    l2 = build([1, 3, 4])
    print(values(Solution().mergeTwoLists(l1, l2)))
# DEBUG RUNNER END
