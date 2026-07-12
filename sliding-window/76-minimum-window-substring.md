# 76. Minimum Window Substring

- **Difficulty:** Hard
- **Pattern:** sliding-window
- **Companies:** Amazon, Google, Meta, Microsoft, Uber, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/minimum-window-substring/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given strings `s` and `t`, return the shortest substring of `s` that contains
every character of `t` (including multiplicities), or `""` if none exists.

## Approaches

### Brute force

Enumerate every substring of `s` and check whether it covers `t`'s character
counts.

- Time: `O(n^2 * |t|)`
- Space: `O(|t|)`

### Optimal

Keep a counter of the still-needed characters, seeded from `t`. Expand `right`
and decrement the count of the current character. While every count is `<= 0`
(all requirements met), record the smallest window and shrink from `left`,
restoring the count of any character that belongs to `t`.

- Time: `O(n * A)` where `A` is the alphabet size checked by the `all(...)` test
- Space: `O(|t|)`

## Key insight

A signed counter lets negatives represent surplus characters, so "is the window
valid?" is simply "are all needed counts satisfied?" and shrinking greedily finds
the minimum length.

## Edge cases

- `t` longer than `s` (return `""`).
- Repeated characters in `t` that must all be covered.
- `s` and `t` equal.

## Pitfalls

- The `all(count <= 0 ...)` validity check is `O(alphabet)` each step; a running
  "formed" counter would make it truly `O(n)`.
- Restoring counts only for characters that are in `target` when shrinking.
- Using `if` instead of `while` to shrink and missing the smallest window.

## Related problems

- 3 Longest Substring Without Repeating Characters
- 438 Find All Anagrams in a String
- 209 Minimum Size Subarray Sum
