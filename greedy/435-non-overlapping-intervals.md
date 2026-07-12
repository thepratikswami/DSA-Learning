# 435. Non-overlapping Intervals

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/non-overlapping-intervals/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the minimum number of intervals to remove so that the remaining intervals
do not overlap.

## Approaches

### Brute force

Try every subset of intervals and keep the largest non-overlapping one; remove the
rest. Exponential.

- Time: `O(2^n)`
- Space: `O(n)`

### Optimal

Sort by end time. Scan while tracking the end of the last kept interval. If the
next interval starts at or after that end, keep it and advance the end; otherwise
it overlaps, so count a removal. This is the classic activity-selection greedy.

- Time: `O(n log n)` for the sort
- Space: `O(1)` beyond the sort

## Key insight

Keeping the interval that finishes earliest leaves the most room for later
intervals, so sorting by end time and greedily accepting compatible ones is
provably optimal.

## Edge cases

- Empty or single interval -> `0` removals.
- Touching intervals like `[1,2]` and `[2,3]` do not overlap.
- All identical intervals -> remove all but one.

## Pitfalls

- Sorting by start time instead of end time.
- Treating shared endpoints as overlaps (use `start >= end`).
- Counting kept intervals instead of removed ones.

## Related problems

- 452 Minimum Number of Arrows to Burst Balloons
- 56 Merge Intervals
- 253 Meeting Rooms II
- 646 Maximum Length of Pair Chain
