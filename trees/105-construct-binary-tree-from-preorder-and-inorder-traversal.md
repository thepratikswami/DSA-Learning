# 105. Construct Binary Tree from Preorder and Inorder Traversal

- **Difficulty:** Medium
- **Pattern:** trees
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Meta
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Rebuild a binary tree given its preorder and inorder traversals, assuming all
values are unique.

## Approaches

### Brute force

For each root taken from preorder, linearly scan inorder to find its split point
and slice the arrays for the recursive calls.

- Time: `O(n^2)`
- Space: `O(n)`

### Optimal

Precompute a `value -> inorder index` map. Walk preorder left to right with a
moving pointer; each value becomes a root, and its inorder index splits the
current inorder range into left and right subtrees.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Preorder gives roots in the exact order they should be created, and the inorder
index map turns "where does this root split the range?" into an `O(1)` lookup, so
no array slicing is needed.

## Edge cases

- Empty input returns `None`.
- Single element becomes a leaf.
- Fully left- or right-skewed traversals.

## Pitfalls

- Advancing the preorder pointer at the wrong time or not sharing it via
  `nonlocal`.
- Slicing arrays (extra `O(n)` copies) instead of passing index bounds.
- Recursing right before left, which breaks the preorder consumption order.

## Related problems

- 106 Construct Binary Tree from Inorder and Postorder Traversal
- 889 Construct Binary Tree from Preorder and Postorder Traversal
- 1008 Construct Binary Search Tree from Preorder Traversal
