# 187. Repeated DNA Sequences

- **Difficulty:** Medium
- **Pattern:** sliding-window
- **Companies:** Amazon, Google, Microsoft, LinkedIn, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/repeated-dna-sequences/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a DNA string `s`, return every length-10 substring that appears more than
once in `s`.

## Approaches

### Brute force

Compare every 10-letter substring against every other substring for equality.

- Time: `O(n^2 * 10)`
- Space: `O(n)`

### Optimal

Slide a fixed-size window of length 10 across the string. Keep a `seen` set of
substrings; the first time a window repeats, add it to a `repeated` set. Return
the repeated set as a list.

- Time: `O(n)` (each 10-char slice hashed once; slice cost treated as constant)
- Space: `O(n)`

## Key insight

A fixed window plus a hash set turns "have I seen this exact substring before?"
into an `O(1)` membership test, and a separate result set naturally deduplicates.

## Edge cases

- Strings shorter than 10 characters (empty result).
- A sequence repeated three or more times (still reported once).
- No repeats at all.

## Pitfalls

- Iterating `range(len(s) - 9)` off by one and missing or overrunning the last
  window.
- Returning duplicates by appending to a list instead of using a set.

## Related problems

- 3 Longest Substring Without Repeating Characters
- 438 Find All Anagrams in a String
- 76 Minimum Window Substring
