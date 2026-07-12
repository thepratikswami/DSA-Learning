# 853. Car Fleet

- **Difficulty:** Medium
- **Pattern:** monotonic-stack
- **Companies:** Amazon, Google, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/car-fleet/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Cars head to a `target` along a one-lane road. A faster car catching a slower one
forms a fleet moving at the slower car's speed and cannot pass. Return the number
of car fleets that reach the target.

## Approaches

### Brute force

Simulate positions over time and merge cars as they collide.

- Time: `O(n^2)` or worse
- Space: `O(n)`

### Optimal

Sort cars by position descending (closest to target first). Compute each car's
arrival time `(target - pos) / speed`. Walk a monotonic stack of arrival times:
a car starts a new fleet only if its arrival time is strictly greater than the
fleet ahead; otherwise it merges. The answer is the number of stack entries.

- Time: `O(n log n)` (from the sort)
- Space: `O(n)`

## Key insight

Ordering by position lets arrival time alone decide fleets: if a car behind
arrives no later than the car ahead, it catches up and joins that fleet.

## Edge cases

- Two cars at the same starting position (avoid duplicate positions in input;
  sorting by position keeps them adjacent so the later one merges).
- Single car -> one fleet.
- A faster car behind a slower one with equal arrival time -> merges.

## Pitfalls

- Using integer division and losing precision; use float division for time.
- Comparing arrival times in the wrong direction after sorting.

## Related problems

- 739 Daily Temperatures (stack)
- 901 Online Stock Span (monotonic-stack)
- 496 Next Greater Element I (monotonic-stack)
