# 417. Pacific Atlantic Water Flow

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Meta, Microsoft, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `m x n` grid of heights, water flows from a cell to an adjacent cell of
equal or lower height. The Pacific touches the top and left edges; the Atlantic
touches the bottom and right edges. Return all cells from which water can reach
both oceans.

## Approaches

### Brute force

From every cell run a search to test whether it can reach each ocean.

- Time: `O((m * n)^2)`
- Space: `O(m * n)`

### Optimal

Invert the flow: start from each ocean's border cells and DFS *uphill* (to
neighbors of equal or greater height), marking every cell that ocean can reach.
Run this once per ocean, then intersect the two reachable sets.

- Time: `O(m * n)`
- Space: `O(m * n)`

## Key insight

Searching outward from the oceans instead of inward from each cell collapses the
work from per-cell searches to two full grid traversals.

## Edge cases

- Empty grid or empty first row.
- Single cell reaches both oceans.
- Flat grid where every cell is reachable.

## Pitfalls

- Reversing the comparison: from the border you climb to `>=` neighbors, not
  `<=`.
- Forgetting a cell already in the reachable set, causing redundant recursion.

## Related problems

- 200 Number of Islands
- 130 Surrounded Regions
- 994 Rotting Oranges
