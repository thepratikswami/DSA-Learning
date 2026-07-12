# 684. Redundant Connection

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Google, Amazon, Meta, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/redundant-connection/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

A tree of `n` nodes had one extra edge added, forming exactly one cycle. Return the
edge that can be removed, choosing the last one in input order if there are several.

## Approaches

### Brute force

For each edge, remove it and check with DFS/BFS whether the remaining graph is still
connected and acyclic. Re-running traversal per edge is costly.

- Time: `O(n^2)`
- Space: `O(n)`

### Optimal

Union-Find with path compression and union by rank. Process edges in order and try
to union each pair; the first edge whose two endpoints already share a root is the
redundant one that closes a cycle.

- Time: `O(n * α(n))` ≈ `O(n)`
- Space: `O(n)`

## Key insight

Adding an edge between two nodes already in the same set is exactly what creates a
cycle, so union-find detects the redundant edge the moment a union fails.

## Edge cases

- The redundant edge is the last edge given.
- Nodes are 1-indexed, so size arrays need `len(edges) + 1`.

## Pitfalls

- Off-by-one sizing of `parent`/`rank` for 1-indexed nodes.
- Skipping path compression or union by rank hurts the near-constant complexity.
- Returning the first cycle edge found by DFS instead of respecting input order.

## Related problems

- 685 Redundant Connection II
- 547 Number of Provinces
- 261 Graph Valid Tree
- 323 Number of Connected Components in an Undirected Graph
