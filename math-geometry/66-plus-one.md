# 66. Plus One

- **Difficulty:** Easy
- **Pattern:** math-geometry
- **Companies:** Amazon, Google, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/plus-one/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a non-empty array of digits representing a non-negative integer (most
significant digit first), increment the integer by one and return the resulting
digit array.

## Approaches

### Brute force

Convert the digit list to an integer, add one, then convert back to a list of
digits. Works but relies on big-integer conversion.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

Walk from the least significant digit. If a digit is `< 9`, increment and return.
Otherwise set it to `0` and carry. If every digit was `9`, prepend a `1`.

- Time: `O(n)`
- Space: `O(1)` extra (only the prepend case allocates)

## Key insight

A carry only propagates while digits equal `9`, so the first digit `< 9` ends the
process; an all-nines number is the sole case that grows in length.

## Edge cases

- All nines, e.g. `[9, 9, 9]` becomes `[1, 0, 0, 0]`.
- Single-digit input like `[0]` or `[9]`.

## Pitfalls

- Forgetting the leading `1` when every digit is `9`.
- Iterating from the most significant digit and mishandling the carry direction.

## Related problems

- 43 Multiply Strings
- 67 Add Binary
- 415 Add Strings
