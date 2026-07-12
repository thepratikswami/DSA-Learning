# 138. Copy List with Random Pointer

- **Difficulty:** Medium
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Meta, Bloomberg, Google
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/copy-list-with-random-pointer/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Each node has a `next` pointer and a `random` pointer that may point to any node or
`None`. Return a deep copy of the list where the clones mirror both pointer sets and
reference only cloned nodes.

## Approaches

### Hash map (two pass)

First pass: create a clone for every original node and store `original -> clone` in a
map (seed it with `None -> None`). Second pass: wire each clone's `next` and `random`
by looking up the mapped clone of the original's pointers.

- Time: `O(n)`
- Space: `O(n)` for the map

### Interleaving (O(1) extra)

Insert each clone directly after its original, set `clone.random = original.random.next`,
then unweave the two lists. Same time, no extra map.

## Key insight

The hard part is `random` pointing anywhere; a map from original node to its clone
lets you resolve any target in `O(1)` regardless of position.

## Edge cases

- Empty list returns `None`.
- `random` pointing to `None` or to the node itself.
- Single node whose `random` points to itself.

## Pitfalls

- Copying `random` before all clones exist (they must all be created first).
- Forgetting the `None -> None` entry, forcing extra null checks.

## Related problems

- 133 Clone Graph
- 1490 Clone N-ary Tree
- 2 Add Two Numbers
