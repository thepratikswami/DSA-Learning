# 322. Coin Change

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/coin-change/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given coin denominations `coins` and an `amount`, return the fewest number of
coins needed to make up that amount, or `-1` if it cannot be made. Each coin may
be used unlimited times.

## Approaches

### Brute force

Recurse on every remaining amount, trying each coin and taking the minimum path.
Without memoization the same sub-amounts are recomputed exponentially.

- Time: `O(amount^coins)` in the worst case
- Space: `O(amount)` recursion depth

### Optimal

Bottom-up DP. `dp[a]` = fewest coins to make amount `a`. Initialize every entry
to a sentinel (`amount + 1`, effectively infinity), set `dp[0] = 0`, then for each
amount `a` relax `dp[a] = min(dp[a], 1 + dp[a - coin])` over all coins that fit.

- Time: `O(amount * len(coins))`
- Space: `O(amount)`

## Key insight

This is an unbounded knapsack: the answer for amount `a` only depends on smaller
amounts, so filling `dp` in increasing order lets each coin be reused freely.

## Edge cases

- `amount == 0` -> `0` coins.
- No combination reaches the amount -> `-1` (sentinel never got relaxed).
- A single coin larger than the amount is simply skipped.

## Pitfalls

- Using `float("inf")` and forgetting the `+ 1` overflows into a valid-looking
  count; the `amount + 1` sentinel avoids arithmetic surprises.
- Confusing "fewest coins" (this problem) with "number of combinations" (518).

## Related problems

- 518 Coin Change II (count combinations)
- 279 Perfect Squares
- 377 Combination Sum IV
