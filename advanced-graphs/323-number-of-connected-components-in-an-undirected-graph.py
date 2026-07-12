from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        components = n
        for a, b in edges:
            if union(a, b):
                components -= 1

        return components


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
# DEBUG RUNNER END
