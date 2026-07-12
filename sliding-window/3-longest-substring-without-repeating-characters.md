# 3. Longest Substring Without Repeating Characters

- **Difficulty:** Medium
- **Pattern:** sliding-window
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Adobe, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s`, return the length of the longest substring that contains no
repeating characters.

## Approaches

### Brute force

Check every substring for uniqueness.

- Time: `O(n^2)` or worse
- Space: `O(n)`

### Optimal (sliding window)

Maintain a window `[left, right]` and a map of each character's last index. When
the current character was seen inside the window, jump `left` past its previous
position. Track the maximum window length.

- Time: `O(n)`
- Space: `O(min(n, alphabet))`

## Key insight

Storing each character's last index lets `left` jump directly past a repeat
instead of sliding one step at a time.

## Edge cases

- Empty string returns `0`.
- Single repeated character returns `1`.

## Pitfalls

- Using `seen[char]` without the `>= left` guard moves `left` backward on stale
  indices.
- Forgetting to update the stored index after moving the window.

## Related problems

- 424 Longest Repeating Character Replacement
- 159 Longest Substring with At Most Two Distinct Characters
- 76 Minimum Window Substring
