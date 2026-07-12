# 152. Maximum Product Subarray

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Microsoft, Google, LinkedIn, Meta
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/maximum-product-subarray/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an integer array `nums`, return the largest product of any contiguous
non-empty subarray.

## Approaches

### Brute force

Compute the product of every subarray `(i, j)` and keep the maximum.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal (Kadane with min/max)

Track both the current maximum and current minimum product ending at each index,
because a negative number swaps them: multiplying the smallest (most negative)
value by a negative yields the new largest. At each element compute
`cur_max = max(num, num*cur_max, num*cur_min)` and the symmetric `cur_min`, then
update the global result.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Unlike max-sum Kadane, a single negative factor can turn the running minimum into
the maximum, so you must carry the minimum alongside the maximum.

## Edge cases

- A single negative element -> that element.
- Zeros reset both running products (the `num` term restarts the window).
- All negatives: an even count can span the whole array; an odd count drops one.

## Pitfalls

- Updating `cur_max` before `cur_min` reads the stale value — compute both from
  the previous pair (tuple assignment) in one step.
- Initializing `result` to `0` fails on all-negative arrays; seed it with
  `max(nums)`.

## Related problems

- 53 Maximum Subarray
- 238 Product of Array Except Self
- 918 Maximum Sum Circular Subarray
