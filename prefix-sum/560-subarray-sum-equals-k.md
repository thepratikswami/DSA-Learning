# 560. Subarray Sum Equals K

- **Difficulty:** Medium
- **Pattern:** prefix-sum
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Count the number of contiguous subarrays whose elements sum to exactly `k`.

## Approaches

### Brute force

Try every start/end pair and sum the range. `O(n^2)` with a running inner sum.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Keep a running prefix sum and a hash map of how many times each prefix has
occurred, seeded with `{0: 1}`. A subarray ending at the current index sums to `k`
exactly when `prefix - k` was seen before, so add `counts[prefix - k]`, then record
the current prefix.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Any subarray sum equals `prefix[j] - prefix[i]`; fixing the right end, the number
of valid left ends is how many earlier prefixes equalled `prefix - k`.

## Edge cases

- Negative numbers and zeros (so sliding window does NOT work here).
- A prefix that itself equals `k` — handled by the `{0: 1}` seed.
- Multiple subarrays sharing the same sum.

## Pitfalls

- Omitting the `{0: 1}` initialization, missing subarrays that start at index 0.
- Updating the map before the lookup, which can count length-0 ranges.
- Reaching for a sliding window — invalid with negatives.

## Related problems

- 974 Subarray Sums Divisible by K
- 523 Continuous Subarray Sum
- 325 Maximum Size Subarray Sum Equals k
- 1 Two Sum
