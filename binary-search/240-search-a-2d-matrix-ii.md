# 240. Search a 2D Matrix II

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Microsoft, Google, Apple, Bloomberg

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/search-a-2d-matrix-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Search a `target` in an `m x n` matrix where every row is sorted left to right and
every column is sorted top to bottom.

## Approaches

### Brute force

Scan every cell, or run a binary search per row.

- Time: `O(m * n)` scan, or `O(m log n)` per-row search
- Space: `O(1)`

### Optimal

Staircase search: start at the top-right corner. If the value equals `target`
return true; if it is greater move left (`col -= 1`), if smaller move down
(`row += 1`). Each step eliminates a full row or column.

- Time: `O(m + n)`
- Space: `O(1)`

## Key insight

At the top-right corner the current value is the largest in its row and the
smallest in its column, so one comparison always rules out an entire row or column.

## Edge cases

- Empty matrix or empty first row.
- Single row or single column.
- Target outside the min/max range of the matrix.

## Pitfalls

- Starting at a corner that is not both a row-max and column-min (top-left or
  bottom-right) breaks the elimination logic.
- Forgetting the bounds check `row < len(matrix) and col >= 0`.

## Related problems

- 74 Search a 2D Matrix
- 378 Kth Smallest Element in a Sorted Matrix
- 704 Binary Search
