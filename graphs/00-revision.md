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

## Worked example

BFS shortest hops from node `0` on the undirected graph
`0-1, 0-2, 1-3, 2-3, 3-4`.

```
adj: 0:[1,2]  1:[0,3]  2:[0,3]  3:[1,2,4]  4:[3]

start: queue=[0]        visited={0}         dist={0:0}
pop 0 -> push 1,2       queue=[1,2]         visited={0,1,2}   dist{1:1,2:1}
pop 1 -> push 3         queue=[2,3]         visited={0,1,2,3} dist{3:2}
pop 2 -> 0,3 seen       queue=[3]
pop 3 -> push 4         queue=[4]           visited+={4}      dist{4:3}
pop 4 -> 3 seen         queue=[]            done
```

Result distances from `0`: `{0:0, 1:1, 2:1, 3:2, 4:3}`. Each node is enqueued once
because it is marked visited on discovery, giving `O(V + E)`.
