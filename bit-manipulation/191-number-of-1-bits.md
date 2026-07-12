# 191. Number of 1 Bits

- **Difficulty:** Easy
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Google, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/number-of-1-bits/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the number of set bits (Hamming weight) in an unsigned integer.

## Approaches

### Brute force

Check each bit with `n & 1` and shift right until `n` becomes 0. Always loops over
all bit positions.

- Time: `O(number_of_bits)` (e.g. 32)
- Space: `O(1)`

### Optimal

Repeatedly apply `n &= n - 1`, which clears the lowest set bit each iteration.
Count how many times this runs — it equals the number of set bits.

- Time: `O(set_bits)` — proportional to the number of 1s, not total bits
- Space: `O(1)`

## Key insight

`n - 1` flips the lowest set bit and all zeros below it; ANDing with `n` erases
exactly that lowest 1, so the loop count is the popcount.

## Edge cases

- `n == 0` -> `0`.
- All bits set -> loops once per bit.

## Pitfalls

- Sign-extension of the top bit in fixed-width signed languages (not an issue in
  Python's arbitrary-precision ints).
- Off-by-one when mixing shifting and the `n & (n-1)` trick.

## Related problems

- 338 Counting Bits
- 461 Hamming Distance
- 231 Power of Two
- 190 Reverse Bits
