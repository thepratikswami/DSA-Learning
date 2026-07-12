# 155. Min Stack

- **Difficulty:** Medium
- **Pattern:** design
- **Companies:** Amazon, Microsoft, Bloomberg, Google, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/min-stack/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum
element `getMin`, all in `O(1)` time.

## Approaches

### Auxiliary min stack

Keep a second stack that stores the current minimum at each level. On `push`,
append `min(val, current_min)`. On `pop`, pop both stacks together so the min
stays aligned with the main stack.

- Time: `O(1)` per operation
- Space: `O(n)`

### Store pairs

Push `(val, current_min)` tuples on a single stack. `getMin` reads the second
element of the top tuple.

- Time: `O(1)` per operation
- Space: `O(n)`

## Key insight

The minimum can only change when you push or pop, so caching the running
minimum at each level makes `getMin` a constant-time read instead of a scan.

## Edge cases

- Pushing equal-to-current-minimum values (use `<=` so duplicates track
  correctly).
- Negative numbers.
- `getMin` immediately after popping the current minimum.

## Pitfalls

- Using `<` instead of `<=`, which loses a duplicate minimum on pop.
- Forgetting to pop the auxiliary stack in lockstep.
- Recomputing the minimum by scanning, breaking `O(1)`.

## Related problems

- 716 Max Stack
- 232 Implement Queue using Stacks
- 225 Implement Stack using Queues
