# 503. Next Greater Element II

- **Difficulty:** Medium
- **Pattern:** monotonic-stack
- **Companies:** Amazon, Google, Bloomberg, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/next-greater-element-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a circular array `nums`, return the next greater element for every index.
The search wraps around the end of the array; return `-1` where none exists.

## Approaches

### Brute force

For each index, scan up to `n - 1` following positions using modulo indexing.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Use a decreasing monotonic stack of indices and iterate `2n` times with
`i % n`. The first pass seeds the stack; the second pass resolves elements whose
next greater value wraps around. Only push indices during the first `n`
iterations.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Simulating one extra loop over the array (`2n` iterations) lets the stack resolve
wrap-around cases without duplicating the data.

## Edge cases

- All equal values -> every answer is `-1` (strict `<` never pops).
- Single element -> `-1`.

## Pitfalls

- Pushing indices during the second pass (would corrupt results).
- Using `<=` instead of `<`, which mishandles equal neighbors.

## Related problems

- 496 Next Greater Element I (monotonic-stack)
- 739 Daily Temperatures (stack)
- 901 Online Stock Span (monotonic-stack)
