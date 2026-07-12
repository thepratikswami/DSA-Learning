# Advanced Graphs Interview Revision

## Core idea

Add weights, ordering, or connectivity to a graph and reach for a specialized
algorithm: union-find for grouping, Dijkstra/Bellman-Ford for shortest paths,
topological sort for dependency order, and Prim/Kruskal for minimum spanning trees.

## How to recognize it

- Edges have weights or costs to minimize.
- There is a limit like "at most k stops" or negative weights are allowed.
- You must connect all nodes at minimum total cost.
- You must output a valid order that respects prerequisites/rules.
- You repeatedly merge sets or count connected components.

## Interview thinking steps

1. Identify the constraint (weights? negatives? hop limit? ordering? connectivity?).
2. Map it to the algorithm: Dijkstra, Bellman-Ford, topo sort, MST, or DSU.
3. Build the graph representation (adjacency list, edge list, or DSU).
4. Run the algorithm; track visited/dist/indegree/parent as needed.
5. Handle disconnected graphs, unreachable nodes, and cycles explicitly.

## Pitfalls

- Using Dijkstra with negative weights (wrong) instead of Bellman-Ford.
- Bellman-Ford without snapshotting distances when a k-edge cap is required.
- Topological sort that ignores cycles (must detect "no valid order").
- Union-find without path compression / union by rank (slow on big inputs).
- MST that forgets a graph may be disconnected (no spanning tree exists).

## Complexity

- Dijkstra (binary heap): `O(E log V)`.
- Bellman-Ford: `O(V * E)`; k-capped variant `O(k * E)`.
- Topological sort (Kahn): `O(V + E)`.
- Prim (heap) / Kruskal (sort + DSU): `O(E log V)` / `O(E log E)`.
- Union-find: near `O(1)` amortized per op with compression + rank.

## Worked example

Bellman-Ford with at most `k = 1` stop, cheapest price from `0` to `2`.
Flights `[[0,1,100],[1,2,100],[0,2,500]]`, so up to `k + 1 = 2` edges allowed.

```
dist = [0, inf, inf]

round 1 (snapshot of dist):        # relax every edge from the frozen snapshot
  0->1 cost 100: dist[1] = 0+100 = 100
  1->2 cost 100: snap[1]=inf, skip
  0->2 cost 500: dist[2] = 0+500 = 500
  dist = [0, 100, 500]

round 2 (snapshot = [0,100,500]):
  0->1 cost 100: 100, no improve
  1->2 cost 100: snap[1]=100 -> dist[2] = min(500, 200) = 200
  0->2 cost 500: no improve
  dist = [0, 100, 200]
```

Answer: `dist[2] = 200`. Snapshotting is essential: it guarantees each round adds
at most one more edge, so after `k + 1` rounds the path uses at most `k` stops.
