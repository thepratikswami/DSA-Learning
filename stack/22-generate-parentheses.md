# 22. Generate Parentheses

- **Difficulty:** Medium
- **Pattern:** stack
- **Companies:** Amazon, Google, Meta, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/generate-parentheses/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `n` pairs of parentheses, generate all combinations of well-formed
parentheses.

## Approaches

### Brute force

Generate every string of length `2n` over `(` and `)`, then filter for validity.

- Time: `O(2^(2n) * n)`
- Space: `O(2^(2n) * n)`

### Optimal (backtracking)

Build the string one character at a time, tracking how many open and close
brackets are placed. Add `(` while `open < n`, add `)` only while
`close < open`. A partial string is only ever a valid prefix, so we never waste
work on impossible branches.

- Time: `O(4^n / sqrt(n))` (the nth Catalan number of results)
- Space: `O(n)` recursion depth (excluding output)

## Key insight

Enforcing `close < open` as an invariant during construction guarantees every
completed string is balanced, replacing generate-then-validate with prune-as-you-go.

## Edge cases

- `n = 1` yields a single result `["()"]`.
- Large `n` grows the result count as the Catalan numbers.

## Pitfalls

- Forgetting to `pop()` after recursing corrupts the shared stack/path.
- Allowing `)` when `close == open` produces invalid strings.

## Related problems

- 20 Valid Parentheses (stack)
- 78 Subsets (backtracking)
- 46 Permutations (backtracking)
