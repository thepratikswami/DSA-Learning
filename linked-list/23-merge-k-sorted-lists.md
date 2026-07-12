# 23. Merge k Sorted Lists

- **Difficulty:** Hard
- **Pattern:** linked-list
- **Companies:** Amazon, Google, Meta, Microsoft, Uber, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/merge-k-sorted-lists/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Merge `k` sorted linked lists into one sorted list and return its head.

## Approaches

### Brute force

Concatenate all nodes, sort by value, then relink. Ignores the existing per-list
order.

- Time: `O(N log N)` where `N` is the total number of nodes
- Space: `O(N)`

### Optimal

Min-heap of the current front node from each list. Seed the heap with each list's
head as `(val, index, node)`, then repeatedly pop the smallest, append it to the
result, and push its successor. The list index breaks ties so nodes are never
compared directly.

- Time: `O(N log k)`
- Space: `O(k)`

## Key insight

At any moment the global minimum is among the `k` list heads, so a size-`k` heap
yields the next output node in `O(log k)`.

## Edge cases

- Empty input list of lists returns `None`.
- Some sublists are empty (`None`) and must be skipped when seeding.
- All lists empty.

## Pitfalls

- Pushing raw `ListNode` objects without a tie-breaker index raises on equal values.
- Forgetting to push `node.next` after popping stops the merge early.
- Not using a dummy head complicates building the result.

## Related problems

- 21 Merge Two Sorted Lists
- 88 Merge Sorted Array
- 148 Sort List
- 373 Find K Pairs with Smallest Sums
