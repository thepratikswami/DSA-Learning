# 130. Surrounded Regions

- **Difficulty:** Medium
- **Pattern:** graphs
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/surrounded-regions/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an `m x n` board of `"X"` and `"O"`, flip every `"O"` region that is fully
surrounded by `"X"` into `"X"`. Regions connected to a border are not captured.
Modify the board in place.

## Approaches

### Optimal

Any `"O"` connected (4-directionally) to a border cell survives. DFS from every
border `"O"`, marking the whole safe component with a temporary sentinel. Then
sweep the board: remaining `"O"` cells are surrounded, so flip them to `"X"`, and
restore the sentinel cells back to `"O"`.

- Time: `O(m * n)`
- Space: `O(m * n)` recursion worst case

## Key insight

It is easier to find what *cannot* be captured (border-connected) than to test
each region for enclosure, so mark survivors first and capture everything left.

## Edge cases

- Empty board or empty first row.
- All `"O"` connected to the border (nothing captured).
- Single row/column where every cell touches a border.

## Pitfalls

- Capturing regions before protecting border-connected ones flips cells that
  should stay.
- Forgetting to restore the sentinel back to `"O"` in the final sweep.

## Related problems

- 200 Number of Islands
- 417 Pacific Atlantic Water Flow
- 733 Flood Fill
