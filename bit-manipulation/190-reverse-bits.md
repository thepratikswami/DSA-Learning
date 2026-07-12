# 190. Reverse Bits

- **Difficulty:** Easy
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Apple, Microsoft, Airbnb
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/reverse-bits/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Reverse the bits of a given 32-bit unsigned integer.

## Approaches

### Optimal (bit shifting)

For each bit position `i` from `0` to `31`, extract bit `i` of `n` and place it at
position `31 - i` in the result by OR-ing it into place.

- Time: `O(1)` (fixed 32 iterations)
- Space: `O(1)`

## Key insight

Position `i` in the input maps to position `31 - i` in the output, so a single
pass over the 32 fixed positions reverses the word without any string conversion.

## Edge cases

- `n = 0` reverses to `0`.
- The high bit set (e.g. `n = 1`) reverses to a large value with the low bit set.

## Pitfalls

- Off-by-one on the target position: it must be `31 - i`, not `32 - i`.
- In languages with signed 32-bit ints, sign extension corrupts the result; in
  Python the width is handled explicitly by the 32-iteration loop.

## Related problems

- 191 Number of 1 Bits (bit-manipulation)
- 338 Counting Bits (bit-manipulation)
- 7 Reverse Integer (bit-manipulation)
