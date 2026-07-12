# 198. House Robber

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Microsoft, Meta, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/house-robber/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given house values in a row, return the maximum you can rob without taking two
adjacent houses.

## Approaches

### Brute force

Try every subset of non-adjacent houses recursively: at each house choose rob or
skip. Exponential without memoization.

- Time: `O(2^n)`
- Space: `O(n)` recursion depth

### Optimal

Track two rolling values while scanning: the best total if we rob the current
house (`skip_prev + num`) and the best if we skip it (`max(rob_prev, skip_prev)`).
Update both in one step, then return their max.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The only state that matters is the best answer including vs. excluding the
previous house, so two scalars replace a full DP array.

## Edge cases

- Empty array -> `0`.
- Single house -> its value.
- All zeros -> `0`.

## Pitfalls

- Updating `rob_prev` before reading it (the simultaneous tuple assignment avoids
  this).
- Assuming greedy "take every other house" — values can make that suboptimal.

## Related problems

- 213 House Robber II
- 337 House Robber III
- 740 Delete and Earn
- 70 Climbing Stairs
