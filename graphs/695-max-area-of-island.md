# 695. Max Area of Island

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/max-area-of-island/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a binary grid, return the area (cell count) of the largest island connected
4-directionally, or `0` if there is no land.

## Approaches

### Optimal

Scan every cell; when land is found, DFS the whole component summing `1` for the
current cell plus the areas returned by its four neighbors, sinking each visited
cell to `0`. Track the running maximum across all components.

- Time: `O(rows * cols)`
- Space: `O(rows * cols)` worst-case recursion depth

## Key insight

The same flood-fill that counts islands can return each component's size; keep the
max instead of a count.

## Edge cases

- Grid with no land returns `0`.
- Single-cell island of area `1`.
- Entire grid is one island.

## Pitfalls

- Forgetting to sink cells leads to double counting and infinite recursion.
- Returning `0` for out-of-bounds/water is what keeps the summation correct.
- Deep recursion stack on large dense grids.

## Related problems

- 200 Number of Islands
- 463 Island Perimeter
- 733 Flood Fill
- 1254 Number of Closed Islands
