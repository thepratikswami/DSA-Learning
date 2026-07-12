# 424. Longest Repeating Character Replacement

- **Difficulty:** Medium
- **Pattern:** sliding-window
- **Companies:** Amazon, Google, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s` and an integer `k`, you may replace at most `k` characters
with any uppercase letter. Return the length of the longest substring containing
a single repeated letter you can obtain.

## Approaches

### Optimal (sliding window)

Grow a window while it stays valid: a window is valid when
`window_length - count_of_most_frequent_char <= k`, meaning the remaining
characters can be replaced within budget. When invalid, shrink from the left.
Track the best window length.

- Time: `O(n)`
- Space: `O(1)` (fixed alphabet)

## Key insight

Only the count of the most frequent character in the window matters; every other
character is a replacement candidate. The window never needs to shrink below the
best length found, so `max_freq` can lag without breaking correctness.

## Edge cases

- `k >= len(s)`: the whole string is achievable.
- Single character string.

## Pitfalls

- Recomputing `max_freq` by scanning counts each step needlessly (not required
  for correctness and slower).
- Using an `if` instead of tracking the running maximum window.

## Related problems

- 3 Longest Substring Without Repeating Characters
- 1004 Max Consecutive Ones III
- 76 Minimum Window Substring
