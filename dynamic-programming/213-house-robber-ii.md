# 213. House Robber II

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Microsoft, Meta, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/house-robber-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Houses are arranged in a circle, so the first and last are adjacent. Return the
maximum you can rob without taking two adjacent houses.

## Approaches

### Brute force

Enumerate every subset of non-adjacent houses under the circular constraint and
take the best total. Exponential.

- Time: `O(2^n)`
- Space: `O(n)`

### Optimal

Because the first and last houses cannot both be robbed, solve two linear House
Robber problems and take the max: one on `nums[1:]` (allow last, skip first) and
one on `nums[:-1]` (allow first, skip last). Each linear pass keeps two rolling
scalars (`rob`, `skip`).

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The circle adds exactly one coupling — first vs. last — so splitting into two
open-row subproblems removes it, and the standard linear DP applies to each.

## Edge cases

- Single house -> its value (both slices would be empty, so handle first).
- Two houses -> the larger one.
- All zeros -> `0`.

## Pitfalls

- Running the linear DP on the full circular array double-counts the adjacent
  first/last pair.
- Forgetting the single-element guard before slicing (`nums[1:]` becomes empty).

## Related problems

- 198 House Robber
- 337 House Robber III
- 740 Delete and Earn
