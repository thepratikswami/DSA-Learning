# 200. Number of Islands

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/number-of-islands/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a 2D grid of `"1"` (land) and `"0"` (water), count the number of islands,
where an island is land connected 4-directionally.

## Approaches

### Optimal

Scan every cell. When an unvisited `"1"` is found, increment the island count and
flood-fill the whole connected component with DFS, sinking each visited land cell
to `"0"` so it is never counted again.

- Time: `O(rows * cols)`
- Space: `O(rows * cols)` worst-case recursion depth

## Key insight

Each new piece of land you reach for the first time starts exactly one island;
flood-fill erases the rest of that component so the outer scan never double-counts.

## Edge cases

- Empty grid or empty first row.
- Grid that is entirely water or entirely land.
- Single-cell grid.

## Pitfalls

- Not marking a cell visited before recursing, causing infinite recursion.
- Mutating the grid may be disallowed; use a separate `visited` set if so.
- Deep recursion can overflow the stack on huge grids; an explicit stack or BFS avoids it.

## Related problems

- 695 Max Area of Island
- 130 Surrounded Regions
- 733 Flood Fill
- 417 Pacific Atlantic Water Flow
