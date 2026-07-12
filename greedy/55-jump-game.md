# 55. Jump Game

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/jump-game/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Each value is the maximum jump length from that index. Return whether you can
reach the last index starting from index 0.

## Approaches

### Brute force

Recurse/DP from each index trying every jump length, marking reachability.
`O(n^2)` or worse.

- Time: `O(n^2)`
- Space: `O(n)`

### Optimal

Scan left to right tracking `farthest`, the furthest index reachable so far. If
the current index ever exceeds `farthest`, it is unreachable -> return `False`.
Otherwise extend `farthest` with `i + nums[i]`. Surviving the scan means the end
is reachable.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

You never need the exact path — only whether the running maximum reach ever falls
behind the current index. A single frontier value decides the answer.

## Edge cases

- Single element -> `True` (already at the end).
- A leading `0` with more elements after -> `False`.
- Zeros that are still covered by an earlier long jump.

## Pitfalls

- Returning early on a `0` without checking whether it is already reachable.
- Comparing against the wrong bound (use `i > farthest`).

## Related problems

- 45 Jump Game II
- 1306 Jump Game III
- 1345 Jump Game IV
- 134 Gas Station
