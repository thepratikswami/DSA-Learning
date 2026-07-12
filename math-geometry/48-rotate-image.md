# 48. Rotate Image

- **Difficulty:** Medium
- **Pattern:** math-geometry
- **Companies:** Amazon, Microsoft, Apple, Google, Facebook
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/rotate-image/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `n x n` 2D matrix, rotate it 90 degrees clockwise. You must rotate the
image **in place**, without allocating another matrix.

## Approaches

### Brute force

Allocate a new `n x n` matrix and place `matrix[i][j]` at `result[j][n-1-i]`,
then copy back.

- Time: `O(n^2)`
- Space: `O(n^2)`

### Optimal

Transpose the matrix across the main diagonal, then reverse each row. Both steps
are in place.

- Time: `O(n^2)`
- Space: `O(1)`

## Key insight

A clockwise 90-degree rotation equals a transpose (reflect over the main
diagonal) followed by a horizontal flip (reverse each row).

## Edge cases

- `1 x 1` matrix stays unchanged.
- Even and odd `n` both work with the transpose/reverse pair.

## Pitfalls

- Transposing every pair twice by looping `j` from `0` instead of `i + 1`.
- Expecting a return value; the method mutates `matrix` in place and returns `None`.

## Related problems

- 54 Spiral Matrix
- 73 Set Matrix Zeroes
- 867 Transpose Matrix
