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

## Worked example

Kth largest with `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`, using a bounded min-heap
of size `k`. Python `heapq` is a min-heap, so the root is the smallest kept value.

1. Push `3`. Heap `[3]`.
2. Push `2`. Heap `[2, 3]`. Size is `2`, not over `k`.
3. Push `1`. Heap `[1, 3, 2]`. Size `3 > 2`, pop min `1`. Heap `[2, 3]`.
4. Push `5`. Heap `[2, 3, 5]`. Size `3 > 2`, pop min `2`. Heap `[3, 5]`.
5. Push `6`. Heap `[3, 5, 6]`. Size `3 > 2`, pop min `3`. Heap `[5, 6]`.
6. Push `4`. Heap `[4, 6, 5]`. Size `3 > 2`, pop min `4`. Heap `[5, 6]`.

The heap holds the two largest values `{5, 6}`; its root `5` is the 2nd largest.
Each push/pop is `O(log k)`, so total work is `O(n log k)`.
