# 13. Roman to Integer

- **Difficulty:** Easy
- **Pattern:** hashing (lookup table)
- **Companies:** Amazon, Microsoft, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/roman-to-integer/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Convert a Roman numeral string to its integer value.

## Approaches

### Optimal

Map each symbol to its value. Scan left to right; if the current symbol's value
is smaller than the next symbol's value it is a subtractive prefix, so subtract
it, otherwise add it.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Roman numerals are additive except when a smaller symbol precedes a larger one;
a single lookahead comparison captures that rule.

## Edge cases

- Subtractive combinations (`IV`, `IX`, `XL`, `XC`, `CD`, `CM`).
- Last character always has no successor (guard the index).

## Pitfalls

- Reading past the end when checking `s[i + 1]`.
- Handling subtractive cases with a second pass instead of the lookahead.

## Related problems

- 12 Integer to Roman
