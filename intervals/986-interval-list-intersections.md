# 986. Interval List Intersections

- **Difficulty:** Medium
- **Pattern:** intervals
- **Companies:** Amazon, Google, Meta, Microsoft
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/interval-list-intersections/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given two lists of closed intervals, each already sorted and pairwise disjoint,
return the intersection of the two lists.

## Approaches

### Optimal (two pointers)

Walk both lists with pointers `i` and `j`. The candidate intersection is
`[max(starts), min(ends)]`; it is valid when `start <= end`. Then advance the
pointer whose interval ends first, since it cannot intersect anything further.

- Time: `O(m + n)`
- Space: `O(1)` (excluding output)

## Key insight

Because both lists are sorted, the interval that ends earliest is exhausted first,
so a single linear sweep with two pointers finds every overlap without sorting.

## Edge cases

- Either list empty -> no intersections.
- Intervals touching at a single point (e.g. `[1, 5]` and `[5, 10]` -> `[5, 5]`).

## Pitfalls

- Using `start < end` instead of `start <= end` drops single-point overlaps.
- Advancing the wrong pointer skips valid intersections.

## Related problems

- 56 Merge Intervals (intervals)
- 57 Insert Interval (intervals)
- 435 Non-overlapping Intervals (intervals)
