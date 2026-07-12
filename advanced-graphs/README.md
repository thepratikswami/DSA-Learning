# Advanced Graphs

## What advanced graph patterns are all about

Advanced graph problems go beyond plain traversal. They add weights, ordering
constraints, or connectivity queries, so the job is picking the right specialized
algorithm: union-find, Dijkstra, Bellman-Ford, topological sort, or an MST builder.

### When to use advanced graph patterns

- Weighted shortest paths with non-negative weights (Dijkstra).
- Shortest paths with negative weights or a hop/stop limit (Bellman-Ford).
- Minimum cost to connect all nodes (Prim or Kruskal MST).
- Ordering with dependencies or lexicographic rules (topological sort).
- Dynamic connectivity, component counts, cycle checks (union-find/DSU).

## Pattern hacks to identify advanced graph problems

- Keywords: `minimum cost to connect`, `cheapest`, `at most k stops`, `order`,
  `dependency`, `connected components`, `network delay`, `swim`, `effort`.
- Edges carry weights or costs you must minimize.
- There is a limit on the number of edges/steps (points at Bellman-Ford).
- You repeatedly merge groups or ask "are these two in the same set?" (DSU).
- You must produce a valid linear order respecting constraints (topo sort).

## Common strategies

- Use union-find (DSU) with path compression and union by rank for connectivity.
- Use Dijkstra with a min-heap for non-negative weighted shortest paths.
- Use Bellman-Ford when weights can be negative or when you cap the number of edges.
- Use topological sort (Kahn's BFS or DFS post-order) for dependency ordering.
- Use Prim's (grow a tree via a min-heap) or Kruskal's (sort edges + DSU) for MST.

## Template

```python
import heapq


def dijkstra(n, adj, src):
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nei, w in adj[node]:
            nd = d + w
            if nd < dist[nei]:
                dist[nei] = nd
                heapq.heappush(heap, (nd, nei))
    return dist


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

## Notes

Pick the algorithm by the constraint, not the surface story. "Non-negative weights
+ shortest path" means Dijkstra; "negative weights or a k-stop cap" means
Bellman-Ford; "connect everything cheaply" means MST; "respect dependencies" means
topological sort; "merge and query groups" means union-find. Build a clean
adjacency list or edge list first, then the algorithm is mostly boilerplate.
