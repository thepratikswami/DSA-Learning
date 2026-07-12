# 295. Find Median from Data Stream

- **Difficulty:** Hard
- **Pattern:** heap
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Support adding numbers from a stream and querying the running median at any time.

## Approaches

### Brute force

Keep a sorted list and insert each new number in order; the median is the middle
element(s).

- Time: `O(n)` per insertion
- Space: `O(n)`

### Optimal

Maintain two heaps: a max-heap `small` for the lower half (stored as negatives)
and a min-heap `large` for the upper half. Push to `small`, move its top to
`large`, then rebalance so `small` is never smaller than `large`. The median is
the top of `small` (odd count) or the average of both tops (even count).

- Time: `O(log n)` per insertion, `O(1)` per query
- Space: `O(n)`

## Key insight

Splitting the data into a lower max-heap and an upper min-heap keeps both middle
values at the heap roots, so the median is always available in `O(1)`.

## Edge cases

- First element (single value is its own median).
- Even vs odd total count.
- Negative numbers, handled by the sign convention on `small`.

## Pitfalls

- Letting the two heaps drift in size without rebalancing.
- Sign mistakes when negating values for the max-heap.

## Related problems

- 480 Sliding Window Median
- 4 Median of Two Sorted Arrays
- 703 Kth Largest Element in a Stream
