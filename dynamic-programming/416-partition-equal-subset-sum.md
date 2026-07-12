# 416. Partition Equal Subset Sum

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/partition-equal-subset-sum/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Decide whether the array can be split into two subsets with equal sum.

## Approaches

### Brute force

Enumerate every subset and test whether its sum equals `total / 2`. Exponential.

- Time: `O(2^n)`
- Space: `O(n)` recursion depth

### Optimal

This is a 0/1 subset-sum. If `total` is odd, return `False`. Otherwise track the
set of reachable sums up to `target = total / 2`; for each number, add it to every
currently reachable sum (capped at `target`). Return `True` as soon as `target`
appears.

- Time: `O(n * target)`
- Space: `O(target)`

## Key insight

Only reachability up to `total / 2` matters — a set (or boolean array) of
achievable sums collapses the exponential search into a pseudo-polynomial pass.

## Edge cases

- Odd total -> immediately `False`.
- Empty array -> `True` (both subsets sum to 0), or per constraints often not
  tested.
- A single large element exceeding half the total -> `False`.

## Pitfalls

- Forgetting the odd-total shortcut.
- Adding a number to sums produced in the *same* iteration (double-using it);
  building a fresh update from the previous set avoids this.
- Not capping reachable sums at `target`, wasting space.

## Related problems

- 494 Target Sum
- 698 Partition to K Equal Sum Subsets
- 1049 Last Stone Weight II
- 322 Coin Change
