# 69. Sqrt(x)

- **Difficulty:** Easy
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Apple, Microsoft, Bloomberg

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/sqrtx/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a non-negative integer `x`, return the integer square root of `x` (the floor
of the true square root), computed without built-in exponent functions.

## Approaches

### Brute force

Increment `i` from `0` while `i * i <= x` and return the last such `i`.

- Time: `O(sqrt(x))`
- Space: `O(1)`

### Optimal

Binary search the candidate root in `[0, x]` with `while left <= right`. Compare
`mid * mid` to `x`, moving `left = mid + 1` when the square is too small and
`right = mid - 1` when too large. On exit `right` holds the floor of the root.

- Time: `O(log x)`
- Space: `O(1)`

## Key insight

`mid * mid` is monotonically increasing in `mid`, so the "is this square <= x"
condition flips exactly once, which is what binary search exploits.

## Edge cases

- `x = 0` and `x = 1` return themselves.
- Perfect squares return the exact root.
- Large `x` where `mid * mid` could overflow in fixed-width languages.

## Pitfalls

- Returning `left` instead of `right` gives the ceiling, not the floor.
- In C/Java, `mid * mid` overflows; use `mid > x / mid` style comparison instead.

## Related problems

- 367 Valid Perfect Square
- 875 Koko Eating Bananas
- 74 Search a 2D Matrix
