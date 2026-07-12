# 704. Binary Search

- **Difficulty:** Easy
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Apple, Bloomberg

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/binary-search/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a sorted array of distinct integers `nums` and a `target`, return its index
or `-1` if it is not present.

## Approaches

### Brute force

Scan every element left to right and compare with `target`.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Classic exact-match binary search with `while left <= right`. Compare `nums[mid]`
to `target`, and discard the half that cannot contain the answer by moving
`left = mid + 1` or `right = mid - 1`.

- Time: `O(log n)`
- Space: `O(1)`

## Key insight

Because the array is sorted, one comparison at `mid` tells you which half to keep,
halving the search space each step.

## Edge cases

- Empty array.
- Single element that is or is not the target.
- Target smaller than first or larger than last element.

## Pitfalls

- Off-by-one in the loop condition: use `left <= right` with inclusive bounds.
- Forgetting to move a boundary can cause an infinite loop.

## Related problems

- 35 Search Insert Position
- 34 Find First and Last Position of Element in Sorted Array
- 33 Search in Rotated Sorted Array
