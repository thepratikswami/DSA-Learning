# 202. Happy Number

- **Difficulty:** Easy
- **Pattern:** math-geometry
- **Companies:** Amazon, Google, Apple, Airbnb, Twitter
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/happy-number/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Repeatedly replace a number by the sum of the squares of its digits. A number is
**happy** if this process reaches `1`; otherwise it loops forever. Return whether
`n` is happy.

## Approaches

### Brute force

Track every number seen in a `set`. If you reach `1` return `True`; if you revisit
a number the sequence cycles, so return `False`.

- Time: `O(log n)` per step, bounded total steps
- Space: `O(log n)` for the visited set

### Optimal

Use Floyd's fast/slow pointers on the digit-square-sum function. If `fast` reaches
`1` the number is happy; if `slow == fast` there is a cycle without `1`.

- Time: `O(log n)` overall
- Space: `O(1)`

## Key insight

The digit-square-sum sequence is a functional graph, so cycle detection (a set or
Floyd's algorithm) decides happiness without unbounded iteration.

## Edge cases

- `n = 1` is happy immediately.
- Single-digit inputs like `7` (happy) versus `2` (unhappy).

## Pitfalls

- Looping forever without cycle detection.
- Initializing `slow` and `fast` to the same value and stopping before the first
  advance.

## Related problems

- 141 Linked List Cycle
- 287 Find the Duplicate Number
- 258 Add Digits
