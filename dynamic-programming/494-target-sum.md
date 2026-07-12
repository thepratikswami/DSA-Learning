# 494. Target Sum

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Meta, Amazon, Google, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/target-sum/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `nums` and a `target`, assign a `+` or `-` sign to each number so the signed
sum equals `target`. Return the number of ways to do so.

## Approaches

### Brute force

Try both signs for every element via recursion (`2^n` sign assignments) and count
the branches whose running total hits `target`.

- Time: `O(2^n)`
- Space: `O(n)` recursion depth

### Optimal (subset-sum DP)

DP over reachable sums. `counts` maps a running total to the number of ways to
reach it. Start at `{0: 1}`; for each `num`, build the next map by adding both
`total + num` and `total - num`. The answer is `counts[target]`. (Equivalently,
reduce to a positive-subset sum `(total + target) / 2` and run 0/1 knapsack.)

- Time: `O(n * S)` where `S` is the range of reachable sums
- Space: `O(S)`

## Key insight

Signs collapse into subset partitioning: choosing `+`/`-` is the same as splitting
`nums` into two groups, so the number of distinct achievable sums is bounded by
the total, not by `2^n`.

## Edge cases

- `target` unreachable (or wrong parity for the subset-sum reduction) -> `0`.
- Zeros double the count for each reachable sum (both signs give the same total).
- Empty `nums` -> `1` way only if `target == 0`.

## Pitfalls

- With the subset-sum reduction, forgetting the parity/`abs(target) > total` check
  produces wrong counts.
- Mutating the running map in place while iterating; build a fresh `defaultdict`
  each step.

## Related problems

- 416 Partition Equal Subset Sum
- 1049 Last Stone Weight II
- 698 Partition to K Equal Sum Subsets
