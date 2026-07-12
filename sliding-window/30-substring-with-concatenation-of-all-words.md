# 30. Substring with Concatenation of All Words

- **Difficulty:** Hard
- **Pattern:** sliding-window
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s` and a list `words` of equal-length words, return all start
indices of substrings that are a concatenation of every word exactly once, in any
order.

## Approaches

### Brute force

For each index, try to greedily peel off `len(words)` words and check the running
frequency against the target counter.

- Time: `O(n * m * k)` for `m` words of length `k`
- Space: `O(m)`

### Optimal

Because all words share length `k`, run `k` independent word-aligned sliding
windows (one per starting offset `0..k-1`). In each, step `right` forward one word
at a time, adding it to a window counter. If a word overflows the target count,
shrink from `left` by whole words until valid; if a word is not in the target,
clear the window and jump `left` past it. Record `left` whenever the window spans
exactly `len(words) * k` characters.

- Time: `O(n * k)`
- Space: `O(m)`

## Key insight

Aligning the window to word boundaries collapses the search to `k` linear scans,
and a frequency counter makes "is this window a valid permutation?" incremental
instead of recomputed each step.

## Edge cases

- Empty `s` or `words`.
- Words with duplicates (target counter must track multiplicities).
- `s` shorter than the total concatenation length.

## Pitfalls

- Sliding one character at a time instead of one word, breaking alignment.
- Forgetting to reset the window when an out-of-vocabulary word appears.
- The `print` debug line in the source is incidental, not part of the algorithm.

## Related problems

- 76 Minimum Window Substring
- 438 Find All Anagrams in a String
- 3 Longest Substring Without Repeating Characters
