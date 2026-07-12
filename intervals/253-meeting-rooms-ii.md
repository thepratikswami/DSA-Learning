# 253. Meeting Rooms II

- **Difficulty:** Medium
- **Pattern:** intervals
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/meeting-rooms-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given meeting intervals, find the minimum number of rooms required to hold all
meetings simultaneously.

## Approaches

### Brute force

Sweep every time point and count how many meetings are active, taking the max.

- Time: `O(n^2)` or `O(n * range)` depending on implementation
- Space: `O(1)` to `O(n)`

### Optimal

Sort meetings by start. Keep a min-heap of end times. For each meeting, if the
earliest ending room (heap top) is free by its start time, reuse it (pop);
otherwise allocate a new room. Push the current end time each iteration. The heap
size is the answer.

- Time: `O(n log n)`
- Space: `O(n)`

## Key insight

The min-heap tracks when rooms free up, so the heap's size at any moment is the
number of concurrently active meetings — the peak is the rooms needed.

## Edge cases

- Empty list needs `0` rooms.
- Touching meetings (`end == next start`) can share a room.
- All meetings overlapping requires `n` rooms.

## Pitfalls

- Comparing `rooms[0] < start` instead of `<=`, forcing extra rooms for
  back-to-back meetings.
- Sorting by end instead of start before the sweep.

## Related problems

- 252 Meeting Rooms
- 56 Merge Intervals
- 1094 Car Pooling
