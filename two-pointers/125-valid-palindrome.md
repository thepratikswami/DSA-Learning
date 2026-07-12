# 125. Valid Palindrome

- **Difficulty:** Easy
- **Pattern:** two-pointers
- **Companies:** Amazon, Microsoft, Facebook, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/valid-palindrome/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s`, return `True` if it reads the same forward and backward after
ignoring case and all non-alphanumeric characters.

## Approaches

### Brute force

Build a filtered, lowercased copy of the string and compare it with its reverse.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

Walk two pointers inward from both ends. Skip non-alphanumeric characters on each
side, then compare the lowercased characters. Any mismatch means it is not a
palindrome.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

You never need a cleaned copy of the string; skipping junk characters in place
lets you compare the two ends directly with constant extra space.

## Edge cases

- Empty string or a string with only non-alphanumeric characters (returns `True`).
- Mixed case letters and embedded digits.
- Single-character strings.

## Pitfalls

- Forgetting the inner `left < right` guard while skipping, which can walk past
  the other pointer.
- Comparing raw characters without normalizing case.

## Related problems

- 680 Valid Palindrome II
- 344 Reverse String
- 5 Longest Palindromic Substring
