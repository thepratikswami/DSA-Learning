# 238. Product of Array Except Self

- **Difficulty:** Medium
- **Pattern:** prefix-sum
- **Companies:** Amazon, Google, Meta, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return an array where each position holds the product of all other elements,
without using division and in `O(n)` time.

## Approaches

### Brute force

For each index multiply every other element. `O(n^2)`.

- Time: `O(n^2)`
- Space: `O(1)` beyond the output

### Optimal

Two passes over a prefix/suffix product. First left-to-right, storing the running
product of everything to the left in `ans[i]`. Then right-to-left, multiplying in
the running product of everything to the right. The output array doubles as the
prefix store, so no extra arrays are needed.

- Time: `O(n)`
- Space: `O(1)` extra (output array excluded)

## Key insight

`answer[i] = (product of left of i) * (product of right of i)`. Computing those
two running products in opposite passes avoids both division and recomputation.

## Edge cases

- Contains one zero -> only that index is nonzero.
- Contains two or more zeros -> all outputs are `0`.
- Negative numbers flip signs correctly.

## Pitfalls

- Using division (fails when a zero is present, and is disallowed).
- Allocating separate prefix and suffix arrays when the output can hold the
  prefix.
- Resetting the running product between the two passes incorrectly.

## Related problems

- 152 Maximum Product Subarray
- 560 Subarray Sum Equals K
- 724 Find Pivot Index
- 42 Trapping Rain Water
