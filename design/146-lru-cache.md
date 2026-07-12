# 146. LRU Cache

- **Difficulty:** Medium
- **Pattern:** design
- **Companies:** Amazon, Microsoft, Google, Meta, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/lru-cache/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a cache with a fixed `capacity` that supports `get(key)` and
`put(key, value)` in `O(1)` average time. When capacity is exceeded, evict the
least-recently-used key. A `get` or `put` on a key marks it most recently used.

## Approaches

### Hash map + doubly linked list

Store each key in a hash map pointing to a node in a doubly linked list ordered
by recency. On access, unlink the node and move it to the front; the tail is
always the least-recently-used entry to evict.

- Time: `O(1)` per operation
- Space: `O(capacity)`

### OrderedDict

Python's `OrderedDict` keeps insertion order and offers `move_to_end` and
`popitem(last=False)`, giving the same behavior with less boilerplate.

- Time: `O(1)` per operation
- Space: `O(capacity)`

## Key insight

The hash map gives `O(1)` lookup while the doubly linked list gives `O(1)`
reordering and eviction. Neither structure alone can do both.

## Edge cases

- `put` on an existing key updates the value and refreshes recency without
  eviction.
- Capacity of 1 evicts on every distinct new key.
- `get` on a missing key returns `-1`.

## Pitfalls

- Forgetting to move a key to most-recent on `get`.
- Deleting the evicted key from the linked list but not the hash map.
- Using an ordinary list, making reordering `O(n)`.

## Related problems

- 460 LFU Cache
- 588 Design In-Memory File System
- 1472 Design Browser History
