# 572. Subtree of Another Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Amazon, Google, Microsoft, Meta, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/subtree-of-another-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given the roots of two trees `root` and `subRoot`, return `True` if `subRoot` is
identical to some subtree of `root` (a node in `root` plus all its descendants).

## Approaches

### DFS + same-tree check

At each node of `root`, run a same-tree comparison against `subRoot`; if any
anchor matches, return `True`.

- Time: `O(m * n)` worst case
- Space: `O(m + n)`

### Serialization + substring search

Serialize both trees with null markers and check whether `subRoot`'s string is a
substring of `root`'s. With KMP this reaches `O(m + n)`.

- Time: `O(m + n)` with KMP
- Space: `O(m + n)`

## Key insight

"Is a subtree" reduces to "is there an anchor node from which the two trees are
identical," so subtree detection is same-tree checking applied at every node.

## Edge cases

- `subRoot` empty is trivially a subtree (`True`).
- `root` empty with non-empty `subRoot` returns `False`.
- Matching values but a partial match (subtree must include all descendants).

## Pitfalls

- Stopping at the first value match without verifying the whole structure.
- Naive serialization where `[12]` can match inside `[1,2]`; delimit values.

## Related problems

- 100 Same Tree
- 101 Symmetric Tree
- 208 Implement Trie (Prefix Tree)
