# 1049. Last Stone Weight II

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/last-stone-weight-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Each turn, smash any two stones together; the difference in weights remains (equal
weights vanish). Return the smallest possible weight of the last remaining stone
(or `0`).

## Approaches

### Brute force

Assign each stone a `+` or `-` sign and minimize the absolute signed sum over all
`2^n` assignments.

- Time: `O(2^n)`
- Space: `O(n)`

### Optimal (subset-sum DP)

Smashing splits the stones into two piles; the result is `|sum(A) - sum(B)|`,
minimized when one pile is as close as possible to `total / 2`. Run a 0/1 knapsack
boolean DP: `dp[s]` = a subset summing to `s` exists. Iterate `s` downward per
stone to reuse each stone once, then the answer is `total - 2 * best` for the
largest reachable `best <= total // 2`.

- Time: `O(n * total)`
- Space: `O(total)`

## Key insight

The sequence of smashes is irrelevant — any `+/-` sign pattern is achievable — so
the problem reduces to partitioning the stones into two groups with the smallest
possible difference.

## Edge cases

- Single stone -> its weight (no pairing possible).
- Perfectly balanced partition -> `0`.
- All equal weights: `0` if the count is even, one stone's weight if odd.

## Pitfalls

- Iterating the inner sum ascending turns 0/1 knapsack into unbounded, letting a
  stone be counted multiple times.
- Returning `best` instead of `total - 2 * best`.

## Related problems

- 416 Partition Equal Subset Sum
- 494 Target Sum
- 1046 Last Stone Weight
