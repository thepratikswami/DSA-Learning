# 739. Daily Temperatures

- **Difficulty:** Medium
- **Pattern:** stack
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/daily-temperatures/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

For each day, find how many days you must wait for a warmer temperature; put `0`
if no warmer day exists.

## Approaches

### Brute force

For each day, scan forward until a warmer temperature is found.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Keep a monotonic decreasing stack of indices. When the current temperature
exceeds the temperature at the stack top, pop and record the index distance as
the answer for that day; then push the current index.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Storing indices (not values) on the stack lets each popped day compute its wait
as `current_index - popped_index` the moment a warmer day arrives.

## Edge cases

- Strictly decreasing temperatures leave every answer at `0`.
- Repeated equal temperatures do not count as warmer.

## Pitfalls

- Using `<=` instead of `<` when popping, which mishandles equal values.
- Storing temperatures instead of indices, losing the distance.

## Related problems

- 496 Next Greater Element I
- 503 Next Greater Element II
- 901 Online Stock Span
