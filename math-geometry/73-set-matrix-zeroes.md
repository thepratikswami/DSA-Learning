# 73. Set Matrix Zeroes

- **Difficulty:** Medium
- **Pattern:** math-geometry
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Oracle
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/set-matrix-zeroes/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `m x n` matrix, if any element is `0`, set its entire row and column to
`0`. Do it **in place**.

## Approaches

### Brute force

Record the coordinates of every zero in two sets (`zero_rows`, `zero_cols`), then
zero out those rows and columns in a second pass.

- Time: `O(m * n)`
- Space: `O(m + n)`

### Optimal

Use the first row and first column as marker storage. Track separately whether
the first row and first column themselves must be zeroed, then apply markers.

- Time: `O(m * n)`
- Space: `O(1)`

## Key insight

The first row and column can double as the `O(m + n)` marker arrays, so no extra
memory is needed once you handle those two lines specially.

## Edge cases

- A zero located in the first row or first column.
- Matrices with a single row or single column.

## Pitfalls

- Zeroing cells during the marking scan, which spreads zeros incorrectly.
- Forgetting the `first_row_zero` / `first_col_zero` flags and clobbering markers.

## Related problems

- 48 Rotate Image
- 289 Game of Life
- 2482 Difference Between Ones and Zeros in Row and Column
