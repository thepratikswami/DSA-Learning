# 252. Meeting Rooms

- **Difficulty:** Easy
- **Pattern:** intervals
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/meeting-rooms/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given meeting time intervals, decide whether a person can attend all of them
without any overlap.

## Approaches

### Brute force

Compare every pair of intervals for overlap.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Sort intervals by start time, then check each adjacent pair: if a meeting starts
before the previous one ends, there is a conflict.

- Time: `O(n log n)`
- Space: `O(1)` extra (ignoring sort)

## Key insight

After sorting by start, the only possible overlap for any meeting is with its
immediate predecessor, so a single linear scan suffices.

## Edge cases

- Empty or single-meeting list returns `True`.
- Touching endpoints (`[0,5]` and `[5,10]`) do not overlap.

## Pitfalls

- Using `<=` instead of `<`, wrongly flagging back-to-back meetings.
- Forgetting to sort before scanning.

## Related problems

- 253 Meeting Rooms II
- 56 Merge Intervals
- 57 Insert Interval
