# 49. Group Anagrams

- **Difficulty:** Medium
- **Pattern:** hashing
- **Companies:** Amazon, Meta, Google, Microsoft, Uber, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/group-anagrams/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Group a list of strings so that words which are anagrams of each other end up in
the same list.

## Approaches

### Brute force

Compare every word with every group's representative by sorting and matching.

- Time: `O(n^2 * k log k)` where `k` is word length
- Space: `O(n * k)`

### Optimal

Build a canonical key for each word and bucket words by that key in a hash map.
Two good keys:

- Sorted characters: `"".join(sorted(word))` — `O(k log k)` per word.
- 26-length letter-count tuple (used in the solution) — `O(k)` per word.

- Time: `O(n * k)` with the count key
- Space: `O(n * k)`

## Key insight

Anagrams share an identical multiset of letters, so any order-independent
fingerprint of the letters can serve as a hash-map key.

## Edge cases

- Empty strings all group together.
- Single-word input.
- Words are lowercase only (the count-array key assumes `a`–`z`).

## Pitfalls

- Using a list as a dict key fails; convert the count array to a `tuple`.
- Assuming input is sorted or unique.

## Related problems

- 242 Valid Anagram
- 438 Find All Anagrams in a String (sliding-window)
