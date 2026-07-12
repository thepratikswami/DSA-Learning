# 778. Swim in Rising Water

- **Difficulty:** Hard
- **Pattern:** advanced-graphs
- **Companies:** Amazon, Google, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/swim-in-rising-water/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `n x n` grid where `grid[r][c]` is the elevation, water rises so at time
`t` you can be on any cell with elevation at most `t`. Starting at `(0, 0)`, return
the least time to reach `(n-1, n-1)`, moving to 4-directional neighbors.

## Approaches

### Brute force

Binary search on time `t` and run a flood fill/BFS at each candidate to test
reachability. Works but repeats traversal for each guessed time.

- Time: `O(n^2 log(max elevation))`
- Space: `O(n^2)`

### Optimal

Dijkstra-style min-heap where a path's cost is the maximum elevation along it. Pop
the cell with the smallest "max elevation so far"; the first time `(n-1, n-1)` is
popped, that value is the answer.

- Time: `O(n^2 log n)`
- Space: `O(n^2)`

## Key insight

Minimize the bottleneck (the largest elevation on the path), not the sum. A min-heap
keyed on `max(path elevation)` extends the safest frontier first.

## Edge cases

- `n == 1`: answer is `grid[0][0]`.
- The start cell's own elevation is a lower bound on the time.

## Pitfalls

- Summing elevations instead of taking the running maximum.
- Not marking cells visited on push, causing repeated heap entries and slowdowns.

## Related problems

- 1631 Path With Minimum Effort
- 743 Network Delay Time
- 787 Cheapest Flights Within K Stops
