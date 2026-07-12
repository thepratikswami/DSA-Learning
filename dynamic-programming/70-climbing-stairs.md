# 70. Climbing Stairs

- **Difficulty:** Easy
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Adobe, Apple, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/climbing-stairs/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

You can climb 1 or 2 steps at a time. Count the distinct ways to reach the top of
`n` stairs.

## Approaches

### Brute force

Recurse `ways(n) = ways(n-1) + ways(n-2)`. Without memoization this recomputes the
same subproblems exponentially.

- Time: `O(2^n)`
- Space: `O(n)` recursion depth

### Optimal

The counts follow the Fibonacci recurrence. Keep two rolling variables and update
`one, two = one + two, one` for `n - 1` iterations, then return `one`.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The number of ways to reach step `i` equals the ways to reach `i-1` plus `i-2`,
which is exactly Fibonacci — so two scalars suffice.

## Edge cases

- `n == 1` -> `1`.
- `n == 2` -> `2`.

## Pitfalls

- Off-by-one in the loop bound (running `n` times instead of `n - 1`).
- Overwriting one variable before using it (the tuple swap avoids this).

## Related problems

- 746 Min Cost Climbing Stairs
- 509 Fibonacci Number
- 91 Decode Ways
- 198 House Robber
