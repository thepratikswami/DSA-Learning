from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        clones = {}

        def dfs(current: "Node") -> "Node":
            if current in clones:
                return clones[current]

            copy = Node(current.val)
            clones[current] = copy
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)


# DEBUG RUNNER START
if __name__ == "__main__":
    # Build the sample graph: 1-2, 1-4, 2-3, 3-4
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = Solution().cloneGraph(n1)

    # Serialize the clone as an adjacency list to prove it is a deep copy.
    visited = {}

    def serialize(node):
        if node.val in visited:
            return
        visited[node.val] = sorted(nb.val for nb in node.neighbors)
        for nb in node.neighbors:
            serialize(nb)

    serialize(cloned)
    print([visited[v] for v in sorted(visited)])
# DEBUG RUNNER END
