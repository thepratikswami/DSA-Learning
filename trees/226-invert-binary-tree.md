# 226. Invert Binary Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Google, Amazon, Microsoft, Apple, Meta
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/invert-binary-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given the root of a binary tree, invert it (mirror it left-to-right) and return
the root.

## Approaches

### Recursive DFS

Swap the left and right children of every node, recursing into each subtree.

- Time: `O(n)`
- Space: `O(h)`

### Iterative BFS

Use a queue; for each dequeued node swap its children and enqueue them.

- Time: `O(n)`
- Space: `O(n)`

## Key insight

Inverting a tree is just swapping children at every node — the recursion handles
the rest because each subtree is inverted independently.

## Edge cases

- Empty tree returns `None`.
- Single node is unchanged.

## Pitfalls

- Reading `root.left` after already reassigning it; do the swap in one tuple
  assignment or cache the value first.
- Forgetting to return the root.

## Related problems

- 100 Same Tree
- 101 Symmetric Tree
- 104 Maximum Depth of Binary Tree
