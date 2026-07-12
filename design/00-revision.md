# Design Interview Revision

## Core idea

Combine simple primitives so that every required operation meets its
complexity target. Usually a hash map provides fast lookup while a second
structure supplies ordering, recency, random access, or ranking.

## How to recognize it

- The prompt says "design" or "implement" a class with named methods.
- Each method has a strict bound such as O(1) or O(log n).
- You need two views of the same data at the same time.
- A single list or dict cannot satisfy every requirement.

## Interview thinking steps

1. List every operation and its required complexity.
2. Pick the structure that makes the hardest operation fast.
3. Add a hash map if you also need O(1) lookup by key.
4. Decide how each mutation keeps all structures in sync.
5. Handle capacity, emptiness, and boundary conditions explicitly.

## Pitfalls

- Forgetting to update the auxiliary structure on every mutation.
- Using `list.remove` or `list.index` (O(n)) inside an O(1) method.
- Off-by-one errors in circular buffer head/tail/count math.
- Not evicting at capacity, or evicting the wrong (not least-recent) item.
- Leaving stale keys in the hash map after deletion.

## Complexity

Most design problems aim for `O(1)` per operation using hash map plus a
linked list or array, or `O(log n)` when a heap is required for ranking.

## Worked example

LRU cache with `capacity = 2`, using an `OrderedDict` where the front is the
least-recently used and the back is the most-recently used.

1. `put(1, 1)`. Cache `{1: 1}`. Order front→back `[1]`.
2. `put(2, 2)`. Cache `{1: 1, 2: 2}`. Order `[1, 2]`. At capacity.
3. `get(1)` returns `1`. Move key `1` to back. Order `[2, 1]`.
4. `put(3, 3)`. Cache is full, so evict the front (least recent) key `2`.
   Insert `3` at back. Cache `{1: 1, 3: 3}`. Order `[1, 3]`.
5. `get(2)` returns `-1` because key `2` was evicted.
6. `put(4, 4)`. Full again, evict front key `1`. Insert `4` at back.
   Cache `{3: 3, 4: 4}`. Order `[3, 4]`.
7. `get(1)` returns `-1` (evicted).
8. `get(3)` returns `3`. Move `3` to back. Order `[4, 3]`.
9. `get(4)` returns `4`. Move `4` to back. Order `[3, 4]`.

Every `get` and `put` touches only the hash map and moves one node, so each
operation is `O(1)`.
