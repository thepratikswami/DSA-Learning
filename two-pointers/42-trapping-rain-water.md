# 42. Trapping Rain Water

- **Difficulty:** Hard
- **Pattern:** two-pointers
- **Companies:** Amazon, Google, Meta, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/trapping-rain-water/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an elevation map `height`, compute how much rainwater is trapped between
the bars after it rains.

## Approaches

### Brute force

For every index, scan left and right to find the tallest bar on each side; the
trapped water there is `min(leftMax, rightMax) - height[i]`.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

Run two pointers inward. Track `left_max` and `right_max`. The shorter side is
the limiting wall, so process whichever pointer has the smaller current height:
add `side_max - height[pointer]` and advance that pointer.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Water above a bar is bounded by the smaller of the two side maxima. Advancing the
smaller side guarantees its `side_max` is the true bound, so the running max on
that side is sufficient.

## Edge cases

- Empty or single-bar arrays (no water).
- Monotonic increasing or decreasing profiles (no water).
- Flat plateaus.

## Pitfalls

- Updating the max *after* adding water, which can double-count or undercount.
- Advancing the taller side, where `side_max` may not yet be the real bound.

## Related problems

- 11 Container With Most Water
- 84 Largest Rectangle in Histogram
- 407 Trapping Rain Water II
