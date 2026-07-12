# 50. Pow(x, n)

- **Difficulty:** Medium
- **Pattern:** math-geometry
- **Companies:** Amazon, Google, Facebook, LinkedIn, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/powx-n/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Implement `pow(x, n)`, which computes `x` raised to the power `n`, where `n` is a
signed 32-bit integer.

## Approaches

### Brute force

Multiply `x` by itself `|n|` times, inverting the result if `n` is negative.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Fast exponentiation by squaring: while the exponent is nonzero, multiply the
result by the current base when the low bit is set, then square the base and
shift the exponent right. Handle negative `n` by using `1 / x` and `-n`.

- Time: `O(log n)`
- Space: `O(1)` iterative (recursive is `O(log n)` stack)

## Key insight

Squaring the base while halving the exponent means each bit of `n` is processed
once, turning `O(n)` multiplications into `O(log n)`.

## Edge cases

- `n = 0` returns `1.0`.
- Negative exponents, including `INT_MIN`; taking the reciprocal avoids overflow
  in Python since integers are unbounded.

## Pitfalls

- Forgetting the reciprocal for negative exponents.
- Deep recursion causing stack overflow for very large `|n|` in languages with a
  fixed stack; the iterative form avoids it.

## Related problems

- 69 Sqrt(x)
- 372 Super Pow
- 1922 Count Good Numbers
