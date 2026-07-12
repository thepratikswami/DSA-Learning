# 40. Combination Sum II

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/combination-sum-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a collection `candidates` (which may contain duplicates) and a `target`,
return all unique combinations where the candidates sum to `target`. Each number
in `candidates` may be used **at most once** in a combination.

## Approaches

### Backtracking with duplicate skipping

Sort the candidates so duplicates sit next to each other. Explore combinations by
choosing a candidate and recursing with `i + 1` (each element used once). Within a
recursion level, skip a candidate equal to its predecessor to avoid emitting the
same combination twice. Break early once a candidate exceeds the remaining target.

- Time: `O(2^n)` in the worst case.
- Space: `O(n)` recursion depth (excluding the output).

## Key insight

Sorting plus the `i > start and candidates[i] == candidates[i - 1]` guard prunes
duplicate combinations at each decision level, so the result set stays unique
without a post-processing dedup step.

## Edge cases

- Repeated values that combine differently (e.g. two separate `1`s).
- No combination reaches the target — return an empty list.
- A single candidate equal to the target.

## Pitfalls

- Recursing with `i` instead of `i + 1` would allow reusing an element.
- Skipping duplicates with `i > 0` instead of `i > start` wrongly drops valid
  combinations that legitimately reuse the same value at different depths.

## Related problems

- 39 Combination Sum
- 90 Subsets II
- 216 Combination Sum III
