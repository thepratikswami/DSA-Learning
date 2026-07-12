# 994. Rotting Oranges

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Microsoft, Meta, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/rotting-oranges/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

In a grid, `0` is empty, `1` is a fresh orange, and `2` is rotten. Every minute a
rotten orange rots any fresh orange 4-directionally adjacent to it. Return the
minimum minutes until no fresh orange remains, or `-1` if some can never rot.

## Approaches

### Optimal (multi-source BFS)

Seed a queue with every initially rotten orange and count the fresh ones. Process
the queue level by level; each level is one minute of spreading. When a fresh
orange rots, decrement the fresh count and enqueue it. After BFS, return the
elapsed minutes if no fresh oranges remain, else `-1`.

- Time: `O(m * n)`
- Space: `O(m * n)`

## Key insight

Starting BFS from all rotten oranges at once means every fresh orange is reached
in the fewest minutes possible, and processing whole levels tracks elapsed time.

## Edge cases

- No fresh oranges at the start returns `0`.
- A fresh orange isolated from any rotten one returns `-1`.
- Grid of all empty cells returns `0`.

## Pitfalls

- Counting a minute even when nothing spreads; only advance time while fresh
  oranges are still being rotted.
- Advancing the timer per-orange instead of per-level, inflating the answer.

## Related problems

- 286 Walls and Gates
- 542 01 Matrix
- 1091 Shortest Path in Binary Matrix
