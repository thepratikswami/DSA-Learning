# 703. Kth Largest Element in a Stream

- **Difficulty:** Easy
- **Pattern:** heap
- **Companies:** Amazon, Facebook, Microsoft, Google, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/kth-largest-element-in-a-stream/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a class that tracks the `k`th largest element in a stream. `KthLargest(k,
nums)` initializes with an integer `k` and a starting array. Each `add(val)`
appends `val` to the stream and returns the current `k`th largest element.

## Approaches

### Fixed-size min-heap

Maintain a min-heap of size `k`. The heap always holds the `k` largest values seen
so far, so its root (`heap[0]`) is exactly the `k`th largest. On `add`, push the new
value and pop the smallest whenever the heap exceeds size `k`.

- Time: `O(log k)` per `add`; `O(n log n)` to build initially.
- Space: `O(k)`.

## Key insight

Keeping only the top `k` elements in a min-heap means the smallest of those `k`
(the root) is the answer. Discarding anything smaller is safe because it can never
be the `k`th largest.

## Edge cases

- Initial `nums` shorter than `k`; the heap fills up as values stream in.
- Duplicate values counted individually.
- `k == 1` reduces to tracking the running maximum.

## Pitfalls

- Using a max-heap of everything wastes space and makes each query `O(k)` to pop
  and restore.
- Forgetting to trim the heap back to size `k` after each push.

## Related problems

- 215 Kth Largest Element in an Array
- 347 Top K Frequent Elements
- 973 K Closest Points to Origin
