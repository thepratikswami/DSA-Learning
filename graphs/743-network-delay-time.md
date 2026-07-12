# 743. Network Delay Time

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Uber, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/network-delay-time/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a directed weighted graph and a source `k`, return the time for a signal to
reach all `n` nodes (the maximum shortest-path distance), or `-1` if some node is
unreachable.

## Approaches

### Brute force

Bellman-Ford: relax all `E` edges `V - 1` times to compute shortest paths.

- Time: `O(V * E)`
- Space: `O(V)`

### Optimal

Dijkstra with a min-heap. Push `(0, k)`, then repeatedly pop the closest unfinalized
node, record its distance, and push neighbors with `time + weight`. The answer is the
largest recorded distance if all `n` nodes were reached, else `-1`.

- Time: `O(E log V)`
- Space: `O(V + E)`

## Key insight

Signal arrival time to every node is a single-source shortest-path problem; the
heap always finalizes the currently nearest node, so the first time a node is
popped its distance is optimal.

## Edge cases

- A node unreachable from `k` yields `-1`.
- Multiple edges between the same pair (keep the effective shortest).
- `n == 1` (source only) gives `0`.

## Pitfalls

- Not skipping already-finalized nodes causes stale, longer distances to overwrite.
- Comparing `len(distances)` against `n` (not `n - 1`) to detect full coverage.
- Nodes are 1-indexed.

## Related problems

- 787 Cheapest Flights Within K Stops
- 1631 Path With Minimum Effort
- 778 Swim in Rising Water
- 1514 Path with Maximum Probability
