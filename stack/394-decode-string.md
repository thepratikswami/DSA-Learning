# 394. Decode String

- **Difficulty:** Medium
- **Pattern:** stack
- **Companies:** Google, Amazon, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/decode-string/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Decode a string encoded as `k[encoded]`, where the bracketed substring repeats
`k` times, with arbitrary nesting.

## Approaches

### Optimal

Scan character by character. Build the current segment and current number as you
go. On `[`, push the segment built so far plus the repeat count and reset. On
`]`, pop the previous segment and repeat count, then set the current segment to
`previous + current * repeat`.

- Time: `O(n)` in the length of the decoded output
- Space: `O(n)` for the stack of pending segments

## Key insight

The stack remembers the partial result and multiplier from each enclosing level,
so nested groups resolve inside-out as brackets close.

## Edge cases

- Multi-digit repeat counts such as `12[a]`.
- Deeply nested brackets like `3[a2[c]]`.
- Letters that appear outside any bracket.

## Pitfalls

- Building the number with only a single digit instead of `number * 10 + d`.
- Resetting the current segment and number at the wrong time around brackets.

## Related problems

- 224 Basic Calculator
- 726 Number of Atoms
- 1087 Brace Expansion
