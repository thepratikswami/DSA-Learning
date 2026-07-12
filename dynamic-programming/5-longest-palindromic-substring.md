# 5. Longest Palindromic Substring

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Microsoft, Google, Meta, Adobe, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s`, return the longest contiguous substring that reads the same
forwards and backwards.

## Approaches

### Brute force

Check every substring for the palindrome property and keep the longest.

- Time: `O(n^3)` (n^2 substrings, `O(n)` to verify each)
- Space: `O(1)`

### Optimal (expand around center)

Every palindrome has a center. Iterate over all `2n - 1` centers (each index for
odd length, each gap for even length) and expand outward while the characters
match, tracking the longest span found.

- Time: `O(n^2)`
- Space: `O(1)`

## Key insight

Growing from a center reuses the fact that a palindrome stays a palindrome only if
its outer characters match, so each expansion is `O(1)` work per added pair — no
substring re-scanning.

## Edge cases

- Empty or single-character string -> returns itself.
- Whole string is a palindrome -> returns all of `s`.
- Even-length palindromes require the `(i, i + 1)` center, not just `(i, i)`.

## Pitfalls

- Handling only odd centers misses even-length palindromes like `"abba"`.
- Recording indices after the while-loop exits (when the characters no longer
  match) yields an off-by-one — capture the best span while it still matches.

## Related problems

- 647 Palindromic Substrings
- 516 Longest Palindromic Subsequence
- 131 Palindrome Partitioning
