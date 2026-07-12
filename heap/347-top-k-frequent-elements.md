# 347. Top K Frequent Elements

- **Difficulty:** Medium
- **Pattern:** heap
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the `k` most frequently occurring elements in an array.

## Approaches

### Brute force

Count frequencies, then fully sort the distinct elements by count and take the
top `k`.

- Time: `O(m log m)` where `m` is the number of distinct values
- Space: `O(m)`

### Optimal

Build a frequency map with `Counter`, then use its `most_common(k)`, which uses a
heap internally to pull the `k` highest-count entries without sorting everything.

- Time: `O(m log k)`
- Space: `O(m)`

## Key insight

Only the relative order of the top `k` counts matters, so a size-`k` heap (via
`most_common`) avoids a full sort of all distinct values.

## Edge cases

- `k` equals the number of distinct elements (return all).
- Ties in frequency (any valid ordering is accepted).

## Pitfalls

- Sorting the entire frequency map when only `k` items are needed.
- Confusing element values with their counts when reading heap tuples.

## Related problems

- 215 Kth Largest Element in an Array
- 692 Top K Frequent Words
- 451 Sort Characters By Frequency
