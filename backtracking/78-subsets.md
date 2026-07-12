# 78. Subsets

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/subsets/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array of distinct integers, return the power set — every possible
subset.

## Approaches

### Optimal

Backtrack over start indices. Record the current `path` at the top of every call
(each node of the tree is itself a valid subset), then extend with each element
from `start` onward, recursing with `i + 1` so no element repeats.

- Time: `O(n * 2^n)` — `2^n` subsets, each up to `O(n)` to copy
- Space: `O(n)` recursion depth, excluding the output

## Key insight

Unlike combinations with a fixed size, every node in the recursion tree is a
result, so the answer is appended before the loop rather than only at a base case.

## Edge cases

- Empty input -> `[[]]`.
- Single element -> `[[], [x]]`.

## Pitfalls

- Appending only at leaves, which misses the smaller subsets.
- Using `i + 1` incorrectly (reusing `start` would create duplicates/reuse).
- Appending `path` instead of `path[:]`.

## Related problems

- 90 Subsets II
- 46 Permutations
- 39 Combination Sum
- 77 Combinations
