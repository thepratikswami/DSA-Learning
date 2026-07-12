# 46. Permutations

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/permutations/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array of distinct integers, return all possible orderings of the
elements.

## Approaches

### Optimal

Backtrack while tracking which indices are already `used`. At each level append
any unused number, recurse until `path` has `n` elements, then undo the choice by
popping and clearing the used flag.

- Time: `O(n * n!)` — `n!` permutations, each costing `O(n)` to copy
- Space: `O(n)` recursion depth and used array, excluding the output

## Key insight

A boolean `used` array turns "which elements remain?" into an `O(1)` check, so
every level simply picks one of the still-available numbers.

## Edge cases

- Single-element array -> one permutation.
- Empty array -> one empty permutation `[[]]`.

## Pitfalls

- Forgetting to reset `used[i] = False` after recursion.
- Appending `path` by reference instead of a copy.
- Assuming inputs are distinct when the variant (47) has duplicates and needs
  extra skipping.

## Related problems

- 47 Permutations II
- 31 Next Permutation
- 78 Subsets
- 77 Combinations
