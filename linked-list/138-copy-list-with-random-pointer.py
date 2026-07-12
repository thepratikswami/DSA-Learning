from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        clones = {None: None}

        curr = head
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clones[curr].next = clones[curr.next]
            clones[curr].random = clones[curr.random]
            curr = curr.next

        return clones[head]


# DEBUG RUNNER START
if __name__ == "__main__":
    def build(pairs):
        # pairs: list of [val, random_index] like LeetCode input.
        nodes = [Node(val) for val, _ in pairs]
        for i, (_, rand) in enumerate(pairs):
            if i + 1 < len(nodes):
                nodes[i].next = nodes[i + 1]
            nodes[i].random = nodes[rand] if rand is not None else None
        return nodes[0] if nodes else None

    def serialize(head):
        index = {}
        order = []
        curr = head
        while curr:
            index[curr] = len(order)
            order.append(curr)
            curr = curr.next

        ans = []
        for node in order:
            rand = index[node.random] if node.random else None
            ans.append([node.val, rand])
        return ans

    head = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    print(serialize(Solution().copyRandomList(head)))
# DEBUG RUNNER END
