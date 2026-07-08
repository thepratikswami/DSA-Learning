# Graphs Interview Revision

## Core idea

Represent relationships as nodes and edges, then traverse or process them with the right algorithm.

## How to recognize it

- The problem has edges, prerequisites, connections, grids, or networks.
- You need reachability, components, cycles, or shortest paths.
- A grid cell can move to neighboring cells.

## Interview thinking steps

1. Decide if it is a grid graph or adjacency-list graph.
2. Build the graph if needed.
3. Choose DFS, BFS, topological sort, union-find, or Dijkstra.
4. Track visited nodes to avoid repeats.
5. Handle disconnected components when the graph may not be connected.

## Pitfalls

- Forgetting to mark visited before recursing or enqueueing.
- Treating directed and undirected edges the same.
- Missing disconnected components.
- Using BFS for weighted shortest paths when Dijkstra is needed.

## Complexity

DFS, BFS, and topological sort are usually `O(V + E)`. Grid traversal is usually `O(rows * cols)`.
