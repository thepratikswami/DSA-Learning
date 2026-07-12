from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dist = [float("inf")] * n
        dist[src] = 0

        # At most k stops means at most k + 1 edges.
        for _ in range(k + 1):
            snapshot = dist[:]  # freeze distances from the previous round
            for u, v, price in flights:
                if snapshot[u] != float("inf") and snapshot[u] + price < dist[v]:
                    dist[v] = snapshot[u] + price

        return dist[dst] if dist[dst] != float("inf") else -1


# DEBUG RUNNER START
if __name__ == "__main__":
    print(
        Solution().findCheapestPrice(
            4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
        )
    )
# DEBUG RUNNER END
