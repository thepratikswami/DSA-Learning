# 90. Subsets II

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Facebook, Microsoft, Google, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/subsets-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an integer array `nums` that may contain duplicates, return all possible
subsets (the power set). The solution set must not contain duplicate subsets.

## Approaches

### Backtracking with duplicate skipping

Sort `nums` first. At each recursion level, record the current path as a subset,
then iterate over remaining choices. Skip a value equal to its immediate
predecessor within the same level so duplicate subsets are never generated. Recurse
with `i + 1` because each index is used at most once.

- Time: `O(n * 2^n)` to build and copy all subsets.
- Space: `O(n)` recursion depth (excluding the output).

## Key insight

The `i > start and nums[i] == nums[i - 1]` guard is the only difference from plain
Subsets (78). It ensures the first occurrence of a duplicate leads the branch and
later occurrences at the same level are pruned.

## Edge cases

- All identical elements (e.g. `[2, 2, 2]`).
- Empty input returns `[[]]`.
- No duplicates behaves exactly like problem 78.

## Pitfalls

- Forgetting to sort makes the duplicate check ineffective.
- Using `i > 0` instead of `i > start` removes valid subsets.

## Related problems

- 78 Subsets
- 40 Combination Sum II
- 47 Permutations II
