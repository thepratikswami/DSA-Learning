# 72. Edit Distance

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Google, Amazon, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/edit-distance/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given two strings `word1` and `word2`, return the minimum number of single-
character insertions, deletions, or replacements needed to turn `word1` into
`word2` (Levenshtein distance).

## Approaches

### Brute force

Recurse on the two prefixes: if the current characters match, move both pointers;
otherwise branch over insert/delete/replace and take the min. Overlapping prefix
pairs recompute exponentially.

- Time: `O(3^(m+n))`
- Space: `O(m + n)` recursion depth

### Optimal (2-D DP)

`dp[i][j]` = edit distance between `word1[:i]` and `word2[:j]`. Base cases:
`dp[i][0] = i`, `dp[0][j] = j`. If characters match, `dp[i][j] = dp[i-1][j-1]`;
otherwise `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` for delete,
insert, and replace respectively.

- Time: `O(m * n)`
- Space: `O(m * n)` (reducible to `O(n)` with two rows)

## Key insight

Each cell reuses three neighbors that each represent one edit operation, so the
whole grid solves every prefix pair exactly once.

## Edge cases

- Either string empty -> length of the other (all inserts or all deletes).
- Identical strings -> `0`.
- Completely different strings -> `max(m, n)` (replaces plus length diff).

## Pitfalls

- Mixing up which neighbor is insert vs. delete; both cost `1`, but the direction
  matters if you reconstruct the operations.
- Forgetting to seed the first row and column with `0..n` and `0..m`.

## Related problems

- 1143 Longest Common Subsequence
- 583 Delete Operation for Two Strings
- 161 One Edit Distance
