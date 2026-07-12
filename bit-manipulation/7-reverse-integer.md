# 7. Reverse Integer

- **Difficulty:** Medium
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Apple, Google, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/reverse-integer/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If the
reversed value overflows the signed 32-bit range `[-2^31, 2^31 - 1]`, return `0`.

## Approaches

### Optimal (digit peeling)

Record the sign, work with the absolute value, and repeatedly pop the last digit
with `% 10` while building the reversed number with `* 10 + digit`. Reapply the
sign and return `0` if the result falls outside the 32-bit signed range.

- Time: `O(log10(x))` (number of digits)
- Space: `O(1)`

## Key insight

`% 10` and `// 10` peel and drop the trailing digit, so multiplying the
accumulator by 10 each step rebuilds the number in reverse without any string
conversion.

## Edge cases

- Trailing zeros collapse (e.g. `120` -> `21`).
- Negative inputs keep their sign (e.g. `-123` -> `-321`).
- Values reversing past the 32-bit bound must return `0`.

## Pitfalls

- Checking overflow only after returning misses the required `0` sentinel.
- Python floor division on negatives misbehaves; handling the sign separately and
  operating on `abs(x)` avoids it.

## Related problems

- 8 String to Integer (atoi)
- 9 Palindrome Number
- 190 Reverse Bits (bit-manipulation)
