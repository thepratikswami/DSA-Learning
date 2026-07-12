# 338. Counting Bits

- **Difficulty:** Easy
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Google, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/counting-bits/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

For every integer from `0` to `n`, return an array of the number of set bits in
each.

## Approaches

### Brute force

Call a popcount routine on each value independently.

- Time: `O(n * bits)`
- Space: `O(1)` beyond the output

### Optimal

DP on prior results: `bits[i] = bits[i >> 1] + (i & 1)`. Dropping the lowest bit
(`i >> 1`) is a smaller, already-computed value; add back `1` if the removed bit
was set.

- Time: `O(n)`
- Space: `O(1)` beyond the output array

## Key insight

`i` has the same set bits as `i // 2` plus possibly the lowest bit, so each answer
is built in `O(1)` from an earlier one.

## Edge cases

- `n == 0` -> `[0]`.
- The array has length `n + 1` (inclusive of `n`).

## Pitfalls

- Sizing the array as `n` instead of `n + 1`.
- Using `i >> 1` but forgetting to add `i & 1`.
- Recomputing popcount from scratch, losing the `O(n)` bound.

## Related problems

- 191 Number of 1 Bits
- 190 Reverse Bits
- 461 Hamming Distance
- 231 Power of Two
