# 56. Merge Intervals

- **Difficulty:** Medium
- **Pattern:** intervals
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/merge-intervals/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a list of intervals, merge all overlapping intervals and return the
non-overlapping result.

## Approaches

### Brute force

Repeatedly scan for any two overlapping intervals and merge them until no
overlaps remain.

- Time: `O(n^2)`
- Space: `O(n)`

### Optimal

Sort by start. Walk through the intervals: if the current start is beyond the
last merged interval's end, append it as new; otherwise extend the last merged
interval's end to the max of the two ends.

- Time: `O(n log n)`
- Space: `O(n)` for the output

## Key insight

Once sorted by start, overlaps are always with the most recently merged interval,
so a single pass extending one running interval merges everything.

## Edge cases

- Fully nested intervals (`[1,10]` contains `[2,3]`).
- Touching intervals (`[1,3]` and `[3,5]`) merge into `[1,5]`.
- Single interval.

## Pitfalls

- Using `max` incorrectly and shrinking an interval when the current end is
  smaller than the stored end.
- Forgetting to sort first.

## Related problems

- 57 Insert Interval
- 435 Non-overlapping Intervals
- 986 Interval List Intersections
