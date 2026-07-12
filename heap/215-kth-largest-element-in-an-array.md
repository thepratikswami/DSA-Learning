# 215. Kth Largest Element in an Array

- **Difficulty:** Medium
- **Pattern:** heap
- **Companies:** Amazon, Google, Meta, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the `k`th largest element in an unsorted array (by value, not by distinct
value).

## Approaches

### Brute force

Sort the array and index the `k`th largest.

- Time: `O(n log n)`
- Space: `O(1)` to `O(n)` depending on the sort

### Optimal

Keep a min-heap of size `k`. Push each number and pop the smallest whenever the
heap exceeds `k`, so the heap always holds the `k` largest seen so far. The root
is the answer.

- Time: `O(n log k)`
- Space: `O(k)`

## Key insight

A bounded min-heap of size `k` keeps only the largest `k` values, and its
smallest element is exactly the `k`th largest overall.

## Edge cases

- `k == 1` (maximum) or `k == n` (minimum).
- Duplicate values are counted by position, not distinctness.

## Pitfalls

- Building a max-heap of all `n` values instead of bounding the heap to `k`.
- Popping before the heap actually exceeds size `k`.

## Related problems

- 347 Top K Frequent Elements
- 703 Kth Largest Element in a Stream
- 973 K Closest Points to Origin
