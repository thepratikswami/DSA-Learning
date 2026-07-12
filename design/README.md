# Design

## What data-structure design is all about

Design problems ask you to build a class that supports a specific set of
operations at a required time complexity. The challenge is not a single
algorithm but choosing and combining the right primitives so every operation
hits its target bound.

### When to use design thinking

- The prompt says "design", "implement a class", or lists methods like
  `get`, `put`, `insert`, `remove`, `getRandom`.
- Each operation has a strict complexity target such as O(1) or O(log n).
- You must maintain ordering, recency, frequency, or random access at once.
- A single structure cannot satisfy every requirement alone.

## Pattern hacks to identify design problems

- Keywords: `design`, `implement`, `LRU`, `getRandom`, `constant time`,
  `O(1)`, `data stream`.
- Multiple methods must all be fast, so no single method can be slow.
- You need two views of the same data (e.g. by key and by order).
- A plain list or dict alone breaks one of the complexity targets.

## Common strategies

- Hash map + doubly linked list for O(1) recency (LRU cache).
- Hash map + dynamic array with swap-with-last for O(1) insert/delete/random.
- Auxiliary stack that mirrors the main stack to track a running min or max.
- Heap to merge or rank streams (news feed, top-k, running median).
- Fixed array with head/tail/count pointers for a circular buffer.
- A pointer into an array (or two stacks) for undo/redo and history.

## Template

```python
class Design:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}          # key -> node / index for O(1) lookup
        self.order = []        # or a doubly linked list for ordering

    def query(self, key):
        # O(1) or O(log n) read, then update auxiliary structure
        ...

    def update(self, key, value):
        # keep every helper structure in sync on each mutation
        ...
```

## Notes

The recurring trick is pairing a hash map (fast lookup) with a second
structure that supplies the property the map lacks: order, recency, random
access, or ranking. Keep every auxiliary structure in sync on each mutation
so all operations stay within their promised bounds.
