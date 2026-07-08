# Heap

## What heap is all about

A heap gives fast access to the smallest or largest current item. In Python, `heapq` is a min-heap.

### When to use heap

- Finding top K, kth largest, or kth smallest values.
- Processing items by priority.
- Maintaining a running median.
- Merging sorted streams or lists.

## Pattern hacks to identify heap problems

- Keywords: `top k`, `kth`, `closest`, `median`, `priority`, `smallest`, `largest`.
- You only need the best few items, not a fully sorted list.
- The next item to process depends on priority.

## Common strategies

- Use a min-heap of size `k` for kth largest.
- Use negative values to simulate a max-heap in Python.
- Use two heaps for median problems.
- Store tuples like `(priority, value)` when priority differs from the item.

## Template

```python
import heapq

heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)
```

## Notes

Heap operations cost `O(log k)` or `O(log n)`, which is often better than sorting everything.
