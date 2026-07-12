# 133. Clone Graph

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Meta, Google, Amazon, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/clone-graph/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a reference to a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node holds a value and a list of its neighbors.

## Approaches

### Optimal

Traverse the graph with DFS (or BFS), keeping a hash map from each original node
to its clone. When you first visit a node, create its clone and record it before
recursing so that cycles resolve to the already-created copy instead of looping
forever. Wire up each clone's neighbor list from the recursion results.

- Time: `O(V + E)`
- Space: `O(V)` for the map plus recursion stack

## Key insight

The `original -> clone` map does double duty: it is both the visited set that
stops cycles and the lookup that lets neighbors point at shared clones.

## Edge cases

- `None` input returns `None`.
- Single node with no neighbors.
- Self-referential or fully connected graphs with many cycles.

## Pitfalls

- Recording the clone in the map *after* recursing causes infinite recursion on
  cycles. Insert the clone first, then visit neighbors.
- Creating a new clone per neighbor edge instead of reusing the mapped clone,
  producing duplicated nodes.

## Related problems

- 138 Copy List with Random Pointer
- 200 Number of Islands
- 323 Number of Connected Components in an Undirected Graph
