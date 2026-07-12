# 39. Combination Sum

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Uber, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/combination-sum/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given distinct `candidates` and a `target`, return every unique combination that
sums to `target`. Each candidate may be reused an unlimited number of times.

## Approaches

### Optimal

Sort the candidates, then backtrack. At each call try candidates from `start`
onward; recurse into index `i` (not `i + 1`) so the same number can be reused,
and pass `start = i` to avoid producing permutations of the same multiset. Break
early once a candidate exceeds the remaining target, since sorting guarantees the
rest are larger.

- Time: `O(n^(target/min))` in the worst case (size of the search tree)
- Space: `O(target/min)` recursion depth, excluding the output

## Key insight

Passing `start = i` (instead of restarting at `0`) enforces non-decreasing
combinations, which is what makes each multiset appear exactly once while still
allowing repeats.

## Edge cases

- No combination reaches the target -> return `[]`.
- A single candidate equals the target.
- Large target with a small candidate causes deep recursion.

## Pitfalls

- Recursing with `i + 1`, which forbids reuse (that solves Combination Sum II).
- Restarting the loop at `0`, which yields duplicate permutations.
- Appending `path` instead of `path[:]`.

## Related problems

- 40 Combination Sum II
- 216 Combination Sum III
- 377 Combination Sum IV
- 78 Subsets
