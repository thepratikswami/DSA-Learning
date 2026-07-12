# 268. Missing Number

- **Difficulty:** Easy
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Meta, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/missing-number/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `n` distinct numbers drawn from `[0, n]`, return the one value in that range
that is missing.

## Approaches

### Brute force

Put the numbers in a set and scan `0..n` for the absent one.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

XOR every index `i` with every value `num`, seeding with `n`. Indices `0..n-1` and
present values cancel in pairs, leaving only the missing number. (The Gauss sum
`n*(n+1)/2 - sum(nums)` also works but can overflow in fixed-width languages.)

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The full index set `{0..n}` XORed with the given values differs by exactly the
missing number; everything else pairs up and cancels.

## Edge cases

- Missing `0` or missing `n` (the boundaries) — seeding with `n` covers both.
- Single element `[0]` -> missing `1`; `[1]` -> missing `0`.

## Pitfalls

- Forgetting to seed the accumulator with `n` (or `len(nums)`).
- Overflow with the summation approach in languages with fixed-width ints.

## Related problems

- 136 Single Number
- 448 Find All Numbers Disappeared in an Array
- 41 First Missing Positive
- 287 Find the Duplicate Number
