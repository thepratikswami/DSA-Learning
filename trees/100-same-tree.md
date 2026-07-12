# 100. Same Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Amazon, Google, Microsoft, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/same-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given the roots of two binary trees `p` and `q`, return `True` if they are
structurally identical and every corresponding node has the same value.

## Approaches

### Recursive DFS

Compare the two nodes at each position: both `None` means match, one `None` or a
value mismatch means fail, otherwise recurse on both children.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

Two trees are the same iff their roots match and their left and right subtrees
are each the same — a clean recursive definition.

## Edge cases

- Both trees empty returns `True`.
- One empty and one non-empty returns `False`.
- Same values but different shape returns `False`.

## Pitfalls

- Checking only values and ignoring structure (missing `None` mismatches).
- Comparing by traversal order alone (`[1,2]` preorder can collide across shapes).

## Related problems

- 101 Symmetric Tree
- 572 Subtree of Another Tree
- 226 Invert Binary Tree
