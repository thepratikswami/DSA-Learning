# 34. Find First and Last Position of Element in Sorted Array

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Adobe

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a sorted array, return the first and last index of `target`, or `[-1, -1]`
if it is absent. Must run in `O(log n)`.

## Approaches

### Brute force

Linear scan to find the first and last occurrence.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Use a reusable lower-bound helper `first_at_least(value)` that returns the first
index with `nums[i] >= value`. The start is `first_at_least(target)`; if that index
is out of range or not equal to `target`, return `[-1, -1]`. The end is
`first_at_least(target + 1) - 1`.

- Time: `O(log n)`
- Space: `O(1)`

## Key insight

The range of a value equals `[lowerBound(target), lowerBound(target + 1) - 1]`, so
two lower-bound searches pinpoint both ends without special-casing duplicates.

## Edge cases

- Target absent entirely.
- All elements equal the target.
- Single element array.

## Pitfalls

- Returning immediately on the first match skips the full range; keep searching.
- Forgetting to verify `nums[start] == target` before trusting the bound.

## Related problems

- 35 Search Insert Position
- 704 Binary Search
- 278 First Bad Version
