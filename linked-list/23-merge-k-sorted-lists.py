import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

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

    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    print(values(Solution().mergeKLists(lists)))
# DEBUG RUNNER END
