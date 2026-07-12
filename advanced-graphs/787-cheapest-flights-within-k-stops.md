# 787. Cheapest Flights Within K Stops

- **Difficulty:** Medium
- **Pattern:** advanced-graphs
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/cheapest-flights-within-k-stops/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `n` cities and directed weighted `flights`, find the cheapest price from
`src` to `dst` using at most `k` stops (so at most `k + 1` edges). Return `-1` if
there is no such route.

## Approaches

### Brute force

DFS every path from `src` while tracking remaining stops and accumulated cost.
The branching factor makes this exponential without memoization.

- Time: exponential
- Space: `O(k)` recursion depth

### Optimal

Bellman-Ford limited to `k + 1` relaxation rounds. Each round relaxes every edge
from a **snapshot** of the previous round's distances, guaranteeing each round adds
at most one more edge to the path.

- Time: `O(k * E)`
- Space: `O(n)` for the distance array

## Key insight

Snapshotting `dist` before relaxing is what enforces the hop limit. Without it, a
single round could chain multiple edges and use more than `k` stops.

## Edge cases

- `src == dst`: cost is `0`.
- No reachable path within `k` stops: return `-1`.
- Multiple edges between the same pair with different prices.

## Pitfalls

- Relaxing against the live `dist` instead of a frozen snapshot (over-counts hops).
- Looping `k` times instead of `k + 1` (off-by-one on allowed edges).

## Related problems

- 743 Network Delay Time
- 1514 Path with Maximum Probability
- 778 Swim in Rising Water
