# 12. Integer to Roman

- **Difficulty:** Medium
- **Pattern:** hashing (greedy lookup table)
- **Companies:** Amazon, Microsoft, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/integer-to-roman/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Convert an integer (1–3999) to its Roman numeral string.

## Approaches

### Optimal

Keep a descending list of `(value, symbol)` pairs that already includes the
subtractive forms (`CM`, `CD`, `XC`, `XL`, `IX`, `IV`). Greedily take as many of
each symbol as fit using `divmod`.

- Time: `O(1)` (bounded by the fixed 13-entry table)
- Space: `O(1)`

## Key insight

Baking the six subtractive combinations directly into the value table removes all
special-casing; plain greedy division then works.

## Edge cases

- Boundary values like `4`, `9`, `40`, `1994`.
- Input is guaranteed within `1..3999`.

## Pitfalls

- Omitting subtractive pairs and trying to patch them afterward.
- Wrong ordering of the table (must be strictly descending).

## Related problems

- 13 Roman to Integer
