# 1. Two Sum

- **Difficulty:** Easy
- **Pattern:** hashing
- **Companies:** Amazon, Google, Apple, Microsoft, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/two-sum/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array `nums` and a `target`, return the indices of the two numbers that
add up to `target`. Exactly one valid answer exists.

## Approaches

### Brute force

Check every pair `(i, j)` and test whether `nums[i] + nums[j] == target`.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Walk once through the array keeping a hash map of `value -> index`. For each
`num`, look up whether its complement `target - num` was already seen.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

A hash map turns the "does the complement exist?" question into an `O(1)` lookup,
so a single pass replaces the nested loop.

## Edge cases

- Duplicate values that are each half of the target (e.g. `[3, 3]`, target `6`).
- Negative numbers and zero.

## Pitfalls

- Storing a value in the map before checking its complement can match an element
  with itself. Check first, then insert.
- Returning values instead of indices.

## Related problems

- 167 Two Sum II - Input Array Is Sorted (two-pointers)
- 15 3Sum
- 560 Subarray Sum Equals K
