# 323. Number of Connected Components in an Undirected Graph

- **Difficulty:** Medium
- **Pattern:** advanced-graphs
- **Companies:** Amazon, Google, Meta, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `n` nodes labeled `0..n-1` and a list of undirected `edges`, return the number
of connected components in the graph.

## Approaches

### Brute force

Build an adjacency list and run DFS/BFS from each unvisited node, counting one
component per traversal launch. Correct and `O(V + E)` but needs the full graph.

- Time: `O(V + E)`
- Space: `O(V + E)`

### Optimal

Union-find (DSU) with path compression and union by rank. Start with `n`
components; each edge that unites two different sets reduces the count by one.

- Time: `O(V + E * α(V))` ~ near linear
- Space: `O(V)`

## Key insight

Every successful union merges two groups into one, so the component count is simply
`n` minus the number of unions that actually joined distinct sets.

## Edge cases

- No edges: `n` components.
- Duplicate edges: a repeat union returns `False` and does not lower the count.
- Self-loop `[a, a]`: same-set union, no change.

## Pitfalls

- Decrementing the count on every edge instead of only successful unions.
- Skipping path compression / union by rank, degrading performance on large inputs.

## Related problems

- 547 Number of Provinces
- 200 Number of Islands
- 684 Redundant Connection
