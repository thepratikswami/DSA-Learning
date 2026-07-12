# 402. Remove K Digits

- **Difficulty:** Medium
- **Pattern:** monotonic-stack
- **Companies:** Amazon, Google, Microsoft, Snap
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/remove-k-digits/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a numeric string `num`, remove exactly `k` digits so the resulting number
is the smallest possible. Return it as a string without leading zeros (or `"0"`).

## Approaches

### Brute force

Try every combination of `k` removals and keep the minimum.

- Time: exponential
- Space: exponential

### Optimal

Greedily build an increasing monotonic stack. For each digit, pop larger digits
on top while removals remain (`k > 0`), because a smaller digit earlier lowers
the value most. If `k` is still positive at the end, trim from the tail. Strip
leading zeros and default to `"0"`.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Removing a larger digit that sits before a smaller one yields the biggest
reduction, and a monotonic increasing stack performs exactly those removals in a
single pass.

## Edge cases

- Removing all digits (`k == len(num)`) -> `"0"`.
- Leading zeros after removal (e.g. `"10200"`, `k=1` -> `"200"`).
- Already increasing digits -> trim the last `k` from the end.

## Pitfalls

- Forgetting to trim the tail when digits are non-decreasing.
- Not stripping leading zeros, or returning `""` instead of `"0"`.

## Related problems

- 316 Remove Duplicate Letters (monotonic-stack)
- 1673 Find the Most Competitive Subsequence
- 84 Largest Rectangle in Histogram (stack)
