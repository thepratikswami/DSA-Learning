# 1288. Remove Covered Intervals

- **Difficulty:** Medium
- **Pattern:** intervals
- **Companies:** Amazon, Google, Facebook, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/remove-covered-intervals/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a list of intervals, remove every interval that is covered by another one in
the list. Interval `[a, b)` is covered by `[c, d)` when `c <= a` and `b <= d`.
Return the number of remaining intervals.

## Approaches

### Optimal (sort + greedy)

Sort by start ascending and, on ties, by end descending. Sweep left to right
tracking the largest end seen. An interval survives only when its end strictly
exceeds the running maximum end; otherwise it is covered.

- Time: `O(n log n)`
- Space: `O(1)` (excluding sort)

## Key insight

Sorting by start then by descending end guarantees that when starts tie, the
widest interval comes first, so any later same-start interval is automatically
covered and handled by the single `end > prev_end` test.

## Edge cases

- Intervals sharing a start point (the tie-break rule is essential).
- Identical duplicate intervals (only one is counted).

## Pitfalls

- Forgetting the descending end tie-break wrongly counts covered same-start
  intervals.
- Using `end >= prev_end` instead of `end > prev_end` counts covered intervals.

## Related problems

- 56 Merge Intervals (intervals)
- 435 Non-overlapping Intervals (intervals)
- 452 Minimum Number of Arrows to Burst Balloons (intervals)
