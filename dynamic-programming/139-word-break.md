# 139. Word Break

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/word-break/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string `s` and a dictionary `wordDict`, return `True` if `s` can be
segmented into a space-separated sequence of one or more dictionary words. Words
may be reused.

## Approaches

### Brute force

Recurse from the front: for every prefix that is a dictionary word, recurse on the
remaining suffix. Overlapping suffixes are recomputed, giving exponential time.

- Time: `O(2^n)`
- Space: `O(n)` recursion depth

### Optimal

Bottom-up DP over suffixes. `dp[i]` = can `s[i:]` be segmented. Set
`dp[len(s)] = True`, then for each start `i` (right to left) look for a split `j`
where `s[i:j]` is a word and `dp[j]` is `True`. Store the dictionary in a set for
`O(1)` membership.

- Time: `O(n^2 * L)` where `L` is the average word length for slicing/hashing
- Space: `O(n + total dictionary size)`

## Key insight

Segmentability of a suffix depends only on shorter suffixes, so a 1-D DP indexed
by start position removes the exponential re-exploration.

## Edge cases

- Empty `s` -> `True` (vacuously segmentable).
- A dictionary word not usable because a needed neighbor split fails.
- Repeated words are allowed — no "used" bookkeeping needed.

## Pitfalls

- Not converting `wordDict` to a set leaves membership at `O(dict size)` and can
  TLE.
- Off-by-one on the inner range: `j` must reach `len(s)` so full-suffix words count.

## Related problems

- 140 Word Break II (return all segmentations)
- 472 Concatenated Words
- 279 Perfect Squares
