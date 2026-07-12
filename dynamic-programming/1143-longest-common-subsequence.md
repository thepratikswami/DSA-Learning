# 1143. Longest Common Subsequence

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/longest-common-subsequence/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the length of the longest subsequence common to two strings `text1` and
`text2` (characters in order, not necessarily contiguous).

## Approaches

### Brute force

Recurse on `(i, j)`: if characters match take `1 + solve(i+1, j+1)`, otherwise the
max of skipping one character on either side. Without memoization this is
exponential.

- Time: `O(2^(m+n))`
- Space: `O(m + n)` recursion depth

### Optimal

Fill a 2D table where `dp[i][j]` is the LCS of the suffixes starting at `i` and
`j`. On a match `dp[i][j] = 1 + dp[i+1][j+1]`, else `max(dp[i+1][j], dp[i][j+1])`.
The implementation keeps only two rows (`prev` and `curr`) to reduce memory.

- Time: `O(m * n)`
- Space: `O(n)` with the rolling-row optimization

## Key insight

Each cell depends only on the row below and the column to the right, so a single
`prev` row plus the `curr` row is enough — no full matrix required.

## Edge cases

- Either string empty -> `0`.
- No common characters -> `0`.
- Identical strings -> the full length.

## Pitfalls

- Confusing subsequence with substring (contiguous).
- Wrong iteration direction relative to how `dp` indices are defined.
- Reusing a stale `curr` row instead of resetting it each outer step.

## Related problems

- 1092 Shortest Common Supersequence
- 583 Delete Operation for Two Strings
- 72 Edit Distance
- 300 Longest Increasing Subsequence
