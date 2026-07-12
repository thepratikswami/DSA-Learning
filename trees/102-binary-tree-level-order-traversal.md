# 102. Binary Tree Level Order Traversal

- **Difficulty:** Medium
- **Pattern:** trees
- **Companies:** Amazon, Microsoft, Meta, Bloomberg, LinkedIn
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the values of a binary tree level by level, from top to bottom, as a list
of lists.

## Approaches

### Optimal

BFS with a queue. At each step record the current queue length, then pop exactly
that many nodes to form one level while enqueuing their children.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Snapshotting `len(queue)` at the start of each iteration fixes the boundary of
the current level, so all nodes on one row are grouped before their children.

## Edge cases

- Empty tree returns `[]`.
- Single node returns `[[val]]`.
- Skewed tree still produces one value per level.

## Pitfalls

- Iterating the queue while appending children without capturing the level size
  first mixes levels together.
- Forgetting the `not root` guard before starting BFS.

## Related problems

- 107 Binary Tree Level Order Traversal II
- 103 Binary Tree Zigzag Level Order Traversal
- 199 Binary Tree Right Side View
- 637 Average of Levels in Binary Tree
