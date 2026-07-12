# 297. Serialize and Deserialize Binary Tree

- **Difficulty:** Hard
- **Pattern:** trees
- **Companies:** Amazon, Google, Meta, Microsoft, LinkedIn
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design an algorithm to serialize a binary tree to a string and deserialize that
string back into an identical tree.

## Approaches

### Preorder DFS with null markers

Serialize with a preorder walk, writing a sentinel (`#`) for every `None` child.
Deserialize by consuming tokens in the same preorder, building left then right.

- Time: `O(n)` for both directions
- Space: `O(n)`

### BFS / level-order

Encode level by level (LeetCode's default format). Also `O(n)` but needs explicit
queue bookkeeping and index tracking.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Recording explicit null markers makes the traversal unambiguous, so a single
preorder sequence uniquely reconstructs the tree without needing a second order.

## Edge cases

- Empty tree serializes to just the null marker and round-trips to `None`.
- Negative values and multi-digit values must survive the delimiter split.
- A skewed tree still round-trips correctly.

## Pitfalls

- Using a delimiter that also appears in values; keep values and `#` separated by
  a reserved character like `,`.
- Reading tokens out of order during deserialization (must match serialize order).

## Related problems

- 449 Serialize and Deserialize BST
- 428 Serialize and Deserialize N-ary Tree
- 105 Construct Binary Tree from Preorder and Inorder Traversal
