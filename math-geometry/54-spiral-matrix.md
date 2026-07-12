# 54. Spiral Matrix

- **Difficulty:** Medium
- **Pattern:** math-geometry
- **Companies:** Amazon, Microsoft, Google, Apple, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/spiral-matrix/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `m x n` matrix, return all its elements in spiral order, starting at the
top-left corner and moving clockwise.

## Approaches

### Brute force

Simulate the walk with a direction vector and a visited grid, turning right
whenever the next cell is out of bounds or already seen.

- Time: `O(m * n)`
- Space: `O(m * n)` for the visited grid

### Optimal

Keep four boundaries (`top`, `bottom`, `left`, `right`). Walk right, down, left,
up, shrinking the matching boundary after each edge.

- Time: `O(m * n)`
- Space: `O(1)` extra (excluding the output)

## Key insight

Tracking four shrinking boundaries removes the need for a visited grid because
each layer is peeled off exactly once.

## Edge cases

- Single row or single column matrices.
- Non-square matrices where the last inner layer is a single row or column.

## Pitfalls

- Re-reading the middle row or column: guard the bottom and left passes with
  `if top <= bottom` and `if left <= right`.
- Off-by-one in the reverse ranges when going left or up.

## Related problems

- 48 Rotate Image
- 59 Spiral Matrix II
- 885 Spiral Matrix III
