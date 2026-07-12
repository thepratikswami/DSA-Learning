# 62. Unique Paths

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/unique-paths/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Count the distinct paths from the top-left to the bottom-right of an `m x n` grid
when you may only move right or down.

## Approaches

### Brute force

Recurse from each cell into right and down neighbors, summing paths that reach the
goal. Exponential without memoization.

- Time: `O(2^(m+n))`
- Space: `O(m + n)` recursion depth

### Optimal

Each cell's path count is the sum of the cell above and the cell to the left. Keep
a single row of length `n` initialized to `1`; for each subsequent row update
`row[col] += row[col - 1]` left to right. The answer is `row[-1]`.

- Time: `O(m * n)`
- Space: `O(n)`

## Key insight

`row[col - 1]` already holds the updated (current-row) value while `row[col]`
still holds the previous row, so one array encodes both "left" and "above".

## Edge cases

- `m == 1` or `n == 1` -> exactly one path.
- `1 x 1` grid -> `1`.

## Pitfalls

- Iterating columns right-to-left, which breaks the rolling-row logic.
- Off-by-one when starting loops at `1` vs `0`.
- Integer overflow in fixed-width languages (not an issue in Python).

## Related problems

- 63 Unique Paths II
- 64 Minimum Path Sum
- 980 Unique Paths III
- 120 Triangle
