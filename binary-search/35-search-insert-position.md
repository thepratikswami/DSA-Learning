# 35. Search Insert Position

- **Difficulty:** Easy
- **Pattern:** binary-search
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Adobe

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/search-insert-position/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a sorted array of distinct integers and a `target`, return the index if the
target is found; otherwise return the index where it would be inserted in order.

## Approaches

### Brute force

Walk left to right and return the first index whose value is `>= target`, or
`len(nums)` if none is found.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Lower-bound binary search using the half-open interval `[left, right)` with
`while left < right`. When `nums[mid] < target` move `left = mid + 1`, otherwise
`right = mid`. `left` ends at the first index where `nums[i] >= target`.

- Time: `O(log n)`
- Space: `O(1)`

## Key insight

The insert position is exactly the lower bound: the first index whose value is not
less than the target. A boundary-style binary search finds it directly.

## Edge cases

- Target smaller than all elements returns `0`.
- Target larger than all elements returns `len(nums)`.
- Target already present returns its exact index.

## Pitfalls

- Initializing `right = len(nums)` (not `len(nums) - 1`) so the insert-at-end case
  is representable.
- Mixing `<=` loop with half-open interval leads to out-of-range access.

## Related problems

- 704 Binary Search
- 34 Find First and Last Position of Element in Sorted Array
- 278 First Bad Version
