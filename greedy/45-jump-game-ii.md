# 45. Jump Game II

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Google, Meta, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/jump-game-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Each value is the maximum jump length from that index. Return the minimum number
of jumps to reach the last index (a solution is guaranteed).

## Approaches

### Brute force

DP where `dp[i]` is the fewest jumps to reach `i`, filled by trying every reach
from each index. `O(n^2)`.

- Time: `O(n^2)`
- Space: `O(n)`

### Optimal

Greedy BFS by "levels". Track the `farthest` index reachable and the boundary
`current_end` of the current jump. When the scan index hits `current_end`, we must
jump again, so increment `jumps` and extend `current_end` to `farthest`.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Each jump defines a reachable window; the answer is how many windows it takes to
cover the last index, and each window extends to the farthest point seen so far.

## Edge cases

- Single element -> `0` jumps.
- Loop only to `len(nums) - 1` so arriving at the last index isn't overcounted.
- Values large enough to reach the end in one jump.

## Pitfalls

- Incrementing `jumps` on every index instead of only at the window boundary.
- Iterating through the last index and adding a spurious jump.
- Confusing "reachable" with "landed on".

## Related problems

- 55 Jump Game
- 1306 Jump Game III
- 1345 Jump Game IV
- 134 Gas Station
