# 316. Remove Duplicate Letters

- **Difficulty:** Medium
- **Pattern:** monotonic-stack
- **Companies:** Amazon, Google, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/remove-duplicate-letters/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Remove duplicate letters from `s` so that every letter appears once and the
result is the lexicographically smallest string among all valid orderings.

## Approaches

### Brute force

Enumerate valid subsequences that include each distinct letter once and keep the
smallest.

- Time: exponential
- Space: exponential

### Optimal

Precompute each letter's last occurrence. Scan with a monotonic stack and a
`seen` set. Skip letters already placed. Otherwise, pop any top letter that is
larger than the current one and still appears later (safe to defer), then push
the current letter.

- Time: `O(n)`
- Space: `O(1)` (bounded by the 26-letter alphabet)

## Key insight

You may only pop a bigger character if it reappears later; last-occurrence
indices guarantee correctness while the stack keeps the result smallest.

## Edge cases

- All unique letters -> string returned unchanged (order preserved).
- Repeated blocks (e.g. `"bcabc"` -> `"abc"`).

## Pitfalls

- Popping a character whose last occurrence has passed (it would vanish).
- Forgetting the `seen` set, causing duplicate letters in the output.

## Related problems

- 402 Remove K Digits (monotonic-stack)
- 1081 Smallest Subsequence of Distinct Characters
- 1673 Find the Most Competitive Subsequence
