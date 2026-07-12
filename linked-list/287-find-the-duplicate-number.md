# 287. Find the Duplicate Number

- **Difficulty:** Medium
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Google, Adobe, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/find-the-duplicate-number/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array `nums` of `n + 1` integers where each value is in `[1, n]`, exactly one
value is repeated (possibly more than once). Find that value without modifying the array
and using `O(1)` extra space.

## Approaches

### Floyd's cycle detection

Treat the array as a function `i -> nums[i]`. Because values live in `[1, n]` and there
are `n + 1` slots, following the links forms a cycle whose entrance is the duplicate.
Phase 1: advance `slow` one step and `fast` two steps until they meet. Phase 2: reset
`slow` to `nums[0]` and move both one step at a time; they meet at the duplicate.

- Time: `O(n)`
- Space: `O(1)`

### Binary search on value range

Count how many numbers are `<= mid`; if the count exceeds `mid`, the duplicate is in the
lower half. `O(n log n)` time, `O(1)` space, and it also avoids mutating the array.

## Key insight

The value constraints guarantee the "next index" mapping has a cycle, so linked-list
cycle detection applies directly to a plain array.

## Edge cases

- Duplicate appearing more than twice.
- Duplicate at the array boundaries.
- Minimal input like `[1, 1]`.

## Pitfalls

- Starting both pointers already equal before the first move (start the loop, then move).
- Confusing the meeting point of phase 1 with the cycle entrance; phase 2 is required.

## Related problems

- 141 Linked List Cycle
- 142 Linked List Cycle II
- 268 Missing Number
