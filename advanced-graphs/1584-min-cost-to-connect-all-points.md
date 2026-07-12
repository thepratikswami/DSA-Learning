# 1584. Min Cost to Connect All Points

- **Difficulty:** Medium
- **Pattern:** advanced-graphs
- **Companies:** Amazon, Microsoft, Google, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/min-cost-to-connect-all-points/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `points` on a 2D plane, connect all of them so any point is reachable from
any other. The cost of an edge is the Manhattan distance between two points.
Return the minimum total cost, i.e. the weight of a minimum spanning tree (MST).

## Approaches

### Brute force

Enumerate spanning trees or try all edge subsets and keep the cheapest connected
one. This is exponential and infeasible beyond a handful of points.

- Time: exponential
- Space: `O(n^2)` for the edge list

### Optimal

Run Prim's algorithm on the complete graph. Start from any point, and repeatedly
pull the cheapest edge from a min-heap that reaches an unvisited point, adding its
Manhattan distance to the total until all `n` points are included.

- Time: `O(n^2 log n)` (heap over up to `n^2` edges)
- Space: `O(n)` for visited plus the heap

## Key insight

The graph is complete, so Prim's (grow a tree from a seed) avoids materializing all
`n^2` edges up front and lazily pushes neighbor distances as points are visited.

## Edge cases

- One point (or zero points): cost is `0`.
- Duplicate coordinates yield zero-cost edges.

## Pitfalls

- Adding a node's cost twice: guard with a `visited` check after popping.
- Using Euclidean distance instead of Manhattan `|dx| + |dy|`.

## Related problems

- 1135 Connecting Cities With Minimum Cost
- 1489 Find Critical and Pseudo-Critical Edges in MST
- 323 Number of Connected Components in an Undirected Graph
