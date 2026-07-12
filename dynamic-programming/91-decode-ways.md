# 91. Decode Ways

- **Difficulty:** Medium
- **Pattern:** dynamic-programming
- **Companies:** Meta, Amazon, Microsoft, Google, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/decode-ways/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

A message of digits was encoded with `A -> 1 ... Z -> 26`. Given the digit string
`s`, return the number of ways to decode it back into letters.

## Approaches

### Brute force

Recurse from the front: consume one digit (if not `'0'`) or two digits (if they
form `10..26`), summing the ways from each branch. Overlapping suffixes recompute
exponentially.

- Time: `O(2^n)`
- Space: `O(n)` recursion depth

### Optimal

Fibonacci-style 1-D DP. `curr` = ways to decode `s[:i+1]`. A single digit `s[i]`
adds `curr` (previous) when it is not `'0'`; a valid two-digit `s[i-1:i+1]` in
`10..26` adds `prev`. Roll two scalars forward.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Each position depends only on the previous one or two, exactly like climbing
stairs — but with validity gates for leading zeros and the `26` ceiling.

## Edge cases

- Leading `'0'` -> `0` ways (nothing maps to `0`).
- Embedded `'0'` valid only as part of `10` or `20`; `30`, `07`, etc. -> `0`.
- Whole string of valid single digits -> Fibonacci-like growth.

## Pitfalls

- Treating `"06"` as a valid two-digit decode; only `10..26` count, so a leading
  zero in the pair is invalid.
- Forgetting to zero out `curr` when `s[i] == '0'` before adding the two-digit
  contribution.

## Related problems

- 639 Decode Ways II
- 70 Climbing Stairs
- 509 Fibonacci Number
