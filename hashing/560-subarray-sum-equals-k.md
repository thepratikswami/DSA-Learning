# 560. Subarray Sum Equals K

- **Difficulty:** Medium
- **Pattern:** hashing (prefix sum)
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Count the number of contiguous subarrays whose sum equals `k`. Values may be
negative, so a sliding window does not apply.

## Approaches

### Brute force

Try every subarray `(i, j)` and sum it (or use a running sum per start).

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Track a running prefix sum. A subarray ending at `i` sums to `k` exactly when a
previous prefix equals `prefix - k`. Keep a hash map of prefix-sum frequencies
and add `counts[prefix - k]` at each step. Seed with `{0: 1}` for subarrays that
start at index 0.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

`sum(i..j) == prefix[j] - prefix[i-1]`, so counting equal earlier prefixes turns
the problem into a running hash-map lookup.

## Edge cases

- Negative numbers and zeros (rules out two-pointer/window).
- `k = 0` with runs that cancel out.

## Pitfalls

- Forgetting the `{0: 1}` seed misses subarrays beginning at index 0.
- Updating the map before adding to the answer can double-count.

## Related problems

- 1 Two Sum
- 974 Subarray Sums Divisible by K
- 523 Continuous Subarray Sum
