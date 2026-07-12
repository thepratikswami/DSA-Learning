# 371. Sum of Two Integers

- **Difficulty:** Medium
- **Pattern:** bit-manipulation
- **Companies:** Amazon, Google, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/sum-of-two-integers/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Compute the sum of two integers `a` and `b` without using the `+` or `-`
operators.

## Approaches

### Optimal (bitwise add with carry)

XOR gives the sum without carries; AND shifted left by one gives the carry. Loop,
feeding the carry back in, until there is no carry left. Because Python integers
are unbounded, apply a `0xFFFFFFFF` mask each step to emulate 32-bit wraparound,
then reinterpret the sign bit to recover negative results.

- Time: `O(1)` (bounded by 32-bit width)
- Space: `O(1)`

## Key insight

Addition decomposes into "sum without carry" (`a ^ b`) plus "carry" (`(a & b) << 1`);
iterating this until the carry vanishes reconstructs the true sum using only
bitwise operators.

## Edge cases

- Negative operands and mixed signs (e.g. `-2 + 3`).
- Results whose 32-bit representation has the sign bit set must be converted back
  to a Python negative int.

## Pitfalls

- Skipping the 32-bit mask lets Python's unbounded integers loop forever on
  negative carries.
- Forgetting to reinterpret the sign bit returns a large positive number instead
  of the negative answer.

## Related problems

- 136 Single Number (bit-manipulation)
- 191 Number of 1 Bits (bit-manipulation)
- 7 Reverse Integer (bit-manipulation)
