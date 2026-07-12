# 131. Palindrome Partitioning

- **Difficulty:** Medium
- **Pattern:** backtracking
- **Companies:** Amazon, Facebook, Google, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/palindrome-partitioning/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s`, partition `s` such that every substring of the partition is a
palindrome. Return all possible palindrome partitionings of `s`.

## Approaches

### Backtracking with palindrome checks

From a starting index, try every possible prefix `s[start:end+1]`. If the prefix is
a palindrome, add it to the current path and recurse from `end + 1`. When `start`
reaches the end of the string, the current path is a complete valid partition.

- Time: `O(n * 2^n)` — up to `2^(n-1)` partitions, each costing `O(n)` to build and
  validate.
- Space: `O(n)` recursion depth (excluding the output).

## Key insight

Only recurse into a prefix when it is already a palindrome. This prunes entire
branches early instead of generating all partitions and filtering afterward.

## Edge cases

- Single character string returns `[[c]]`.
- All identical characters produce many partitions.
- No multi-character palindromes — every character becomes its own piece.

## Pitfalls

- Off-by-one slicing: the prefix is `s[start:end + 1]`, and recursion continues at
  `end + 1`.
- Recomputing palindrome checks repeatedly is fine here, but for large inputs a DP
  table `is_pal[i][j]` avoids the extra `O(n)` factor.

## Related problems

- 132 Palindrome Partitioning II (dynamic-programming)
- 5 Longest Palindromic Substring
- 93 Restore IP Addresses
