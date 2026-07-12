# 20. Valid Parentheses

- **Difficulty:** Easy
- **Pattern:** stack
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/valid-parentheses/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a string of brackets `()[]{}`, determine whether every opening bracket is
closed by the same type in the correct order.

## Approaches

### Optimal

Push every opening bracket onto a stack. On each closing bracket, pop and check
that it matches the expected opener; if the stack is empty or the top mismatches,
the string is invalid. A valid string leaves the stack empty at the end.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

The most recently opened bracket must be the first one closed, which is exactly
last-in-first-out order — a stack.

## Edge cases

- Empty string is valid.
- Odd-length strings can never be valid.
- A closing bracket arriving when the stack is empty.

## Pitfalls

- Forgetting the final emptiness check, which lets unclosed openers pass.
- Only counting brackets instead of matching their types and order.

## Related problems

- 22 Generate Parentheses
- 32 Longest Valid Parentheses
- 1249 Minimum Remove to Make Valid Parentheses
