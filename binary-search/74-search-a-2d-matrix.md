# 74. Search a 2D Matrix

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Meta

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/search-a-2d-matrix/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Search a `target` in an `m x n` matrix where each row is sorted and the first
value of each row is greater than the last value of the previous row.

## Approaches

### Brute force

Scan every cell and compare with `target`.

- Time: `O(m * n)`
- Space: `O(1)`

### Optimal

Treat the matrix as one virtually flattened sorted array of length `m * n` and run
standard binary search over indices `[0, m*n - 1]`. Convert index `mid` to a cell
with `matrix[mid // cols][mid % cols]`.

- Time: `O(log(m * n))`
- Space: `O(1)`

## Key insight

The row-major concatenation of the matrix is fully sorted, so a single binary
search over one flat index works; the divmod maps that index back to `(row, col)`.

## Edge cases

- Empty matrix or empty first row.
- Single cell matrix.
- Target smaller than `matrix[0][0]` or larger than the last cell.

## Pitfalls

- Off-by-one in `cols` when computing `mid // cols` and `mid % cols`.
- Using `rows` instead of `cols` for the divmod divisor.

## Related problems

- 240 Search a 2D Matrix II
- 704 Binary Search
- 33 Search in Rotated Sorted Array
