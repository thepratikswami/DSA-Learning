# 300. Longest Increasing Subsequence

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Google, Amazon, Microsoft, Meta, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an integer array `nums`, return the length of the longest strictly
increasing subsequence (elements need not be contiguous).

## Approaches

### Brute force / O(n^2) DP

`dp[i]` = length of the LIS ending at index `i`. For each `i`, scan all `j < i`
and if `nums[j] < nums[i]` take `dp[i] = max(dp[i], dp[j] + 1)`. Answer is
`max(dp)`.

- Time: `O(n^2)`
- Space: `O(n)`

### Optimal (patience sorting)

Maintain `tails`, where `tails[k]` is the smallest possible tail of an increasing
subsequence of length `k + 1`. For each `num`, binary-search (`bisect_left`) the
first tail `>= num`: replace it, or append if `num` is larger than all tails. The
length of `tails` is the LIS length.

- Time: `O(n log n)`
- Space: `O(n)`

## Key insight

`tails` stays sorted, so binary search finds where each number extends or improves
a subsequence. `tails` is not itself a valid LIS, but its length is correct.

## Edge cases

- Empty array -> `0`.
- Strictly decreasing input -> `1`.
- Duplicates: `bisect_left` keeps the subsequence strictly increasing.

## Pitfalls

- Using `bisect_right` would allow equal elements and yield the longest
  non-decreasing subsequence instead of strictly increasing.
- Mistaking `tails` for the actual subsequence — only its length is meaningful.

## Related problems

- 673 Number of Longest Increasing Subsequence
- 354 Russian Doll Envelopes
- 1143 Longest Common Subsequence
