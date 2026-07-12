# 57. Insert Interval

- **Difficulty:** Medium
- **Pattern:** intervals
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, LinkedIn
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/insert-interval/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a sorted, non-overlapping list of intervals, insert a new interval and
merge as needed, keeping the result sorted and non-overlapping.

## Approaches

### Brute force

Append the new interval, re-sort, and run the full merge-intervals routine.

- Time: `O(n log n)`
- Space: `O(n)`

### Optimal

In three phases over the already-sorted input: copy intervals that end before the
new one starts, absorb all intervals that overlap the new one by expanding its
bounds, then append the merged new interval and copy the rest.

- Time: `O(n)`
- Space: `O(n)` for the output

## Key insight

Because the input is already sorted and disjoint, a single linear sweep can place
the new interval without re-sorting — overlaps form one contiguous run.

## Edge cases

- New interval before all or after all existing intervals.
- New interval overlapping nothing (pure insert).
- Empty input list.

## Pitfalls

- Using `<` vs `<=` at the boundaries, mishandling touching intervals.
- Mutating `newInterval` in place while it is also referenced elsewhere.

## Related problems

- 56 Merge Intervals
- 435 Non-overlapping Intervals
- 986 Interval List Intersections
