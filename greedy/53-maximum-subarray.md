# 53. Maximum Subarray

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/maximum-subarray/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an integer array `nums`, find the contiguous subarray (containing at least
one number) that has the largest sum, and return that sum.

## Approaches

### Brute force

Try every start/end pair and sum each subarray.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal (Kadane)

Walk once, tracking the best sum ending at the current index. At each step either
extend the running sum or restart from the current number, whichever is larger.
Keep the global maximum seen so far.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The best subarray ending at index `i` is either just `nums[i]` or `nums[i]` plus
the best subarray ending at `i - 1`. A negative running sum is never worth
carrying forward.

## Edge cases

- All-negative arrays: the answer is the single largest element.
- Single-element arrays.

## Pitfalls

- Initializing the answer to `0` breaks on all-negative input; seed with
  `nums[0]` instead.
- Forgetting the subarray must be non-empty.

## Related problems

- 152 Maximum Product Subarray
- 918 Maximum Sum Circular Subarray
- 121 Best Time to Buy and Sell Stock
