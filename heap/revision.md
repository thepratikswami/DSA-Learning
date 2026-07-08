# Heap Interview Revision

## Core idea

Use a heap when you repeatedly need the smallest, largest, or highest-priority item.

## How to recognize it

- The question asks for top K or kth largest/smallest.
- You need a changing priority queue.
- Sorting all values works but feels heavier than necessary.
- You need median from a stream.

## Interview thinking steps

1. Decide whether you need min-heap, max-heap, or two heaps.
2. Decide what goes into the heap tuple.
3. Keep heap size bounded when only K items matter.
4. Rebalance two heaps when their sizes drift.
5. Explain why full sorting is not required.

## Pitfalls

- Forgetting Python `heapq` is a min-heap.
- Negating values inconsistently for max-heap behavior.
- Comparing tuples whose second element may not be comparable.
- Letting heap size grow when only K values are needed.

## Complexity

Typical top-K solutions are `O(n log k)` time and `O(k)` space.
