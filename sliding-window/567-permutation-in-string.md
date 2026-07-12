# 567. Permutation in String

- **Difficulty:** Medium
- **Pattern:** sliding-window
- **Companies:** Amazon, Microsoft, Google, Facebook
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/permutation-in-string/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given two strings `s1` and `s2`, return whether `s2` contains a permutation of
`s1` as a substring.

## Approaches

### Optimal (fixed-size sliding window)

A permutation of `s1` is any substring of length `len(s1)` with the same
character frequencies. Build a frequency map for `s1` and for the first window of
`s2`, then slide the window one character at a time: add the incoming character,
remove the outgoing one, and compare frequency maps.

- Time: `O(n)`
- Space: `O(1)` (fixed alphabet)

## Key insight

Order does not matter — only character counts. A matching count map over a window
of the right length means that window is a permutation.

## Edge cases

- `len(s1) > len(s2)`: impossible, return `False`.
- Identical strings: `True`.

## Pitfalls

- Comparing `Counter` objects while leaving zero-count keys in the map — delete
  keys when they hit zero so equality holds.
- Off-by-one on the outgoing index `right - len(s1)`.

## Related problems

- 438 Find All Anagrams in a String
- 76 Minimum Window Substring
- 242 Valid Anagram
