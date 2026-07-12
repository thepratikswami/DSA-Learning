# 973. K Closest Points to Origin

- **Difficulty:** Medium
- **Pattern:** heap
- **Companies:** Amazon, Facebook, Google, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array of `points` on a plane and an integer `k`, return the `k` points
closest to the origin `(0, 0)`. Distance is Euclidean. The answer may be returned in
any order.

## Approaches

### Fixed-size max-heap

Keep a max-heap of size `k` keyed by squared distance (negated, since `heapq` is a
min-heap). Push each point and pop the farthest whenever the heap exceeds `k`. What
remains are the `k` closest points.

- Time: `O(n log k)`.
- Space: `O(k)`.

### Alternatives

- Sort all points by distance: `O(n log n)`.
- Quickselect for average `O(n)`.

## Key insight

Comparing **squared** distances avoids costly square roots and preserves ordering.
Bounding the heap at size `k` keeps each insertion at `O(log k)` rather than
`O(log n)`.

## Edge cases

- `k` equals the number of points — return all of them.
- Points on the same distance ring; ties can be broken arbitrarily.
- Negative coordinates handled naturally by squaring.

## Pitfalls

- Taking the real square root is unnecessary and introduces floating-point error.
- Using a min-heap of all points and popping `k` times is `O(n + k log n)` but uses
  `O(n)` space; the bounded max-heap is leaner.

## Related problems

- 215 Kth Largest Element in an Array
- 347 Top K Frequent Elements
- 703 Kth Largest Element in a Stream
