# 724. Find Pivot Index

- **Difficulty:** Easy
- **Pattern:** prefix-sum
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/find-pivot-index/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the leftmost index where the sum of all values to its left equals the sum
of all values to its right, or `-1` if none exists.

## Approaches

### Brute force

For each index, sum the left and right slices separately and compare. `O(n^2)`.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Precompute `total`. Scan while maintaining `left_sum`. At index `i` the right sum
is `total - left_sum - nums[i]`; if it equals `left_sum`, `i` is the pivot. Then
add `nums[i]` to `left_sum`.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The right-side sum never needs its own loop — it is just `total - left_sum -
current`, so one running left sum answers each index in `O(1)`.

## Edge cases

- Pivot at index 0 (empty left, right sum is `0`) or at the last index.
- Empty array -> `-1`.
- Negative numbers are allowed and handled naturally.

## Pitfalls

- Forgetting to exclude `nums[i]` from the right sum.
- Updating `left_sum` before doing the comparison.
- Returning the sum or a boolean instead of the index.

## Related problems

- 1991 Find the Middle Index in Array
- 238 Product of Array Except Self
- 560 Subarray Sum Equals K
- 303 Range Sum Query - Immutable
