# 199. Binary Tree Right Side View

- **Difficulty:** Medium
- **Pattern:** trees
- **Companies:** Meta, Amazon, Google, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/binary-tree-right-side-view/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Imagine standing on the right side of the tree; return the values of the nodes
visible from top to bottom (the last node of each level).

## Approaches

### BFS by level

Run a level-order traversal and record the last node dequeued on each level.

- Time: `O(n)`
- Space: `O(n)`

### DFS right-first

Recurse right before left, appending a node's value the first time a new depth is
reached.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

The right side view is exactly the last node encountered at each depth — either
the tail of each BFS level or the first node seen per depth in a right-first DFS.

## Edge cases

- Empty tree returns `[]`.
- A left-only tree still shows one node per level (the leftmost is rightmost).
- Single node returns that node.

## Pitfalls

- Assuming every visible node is a right child; a level's rightmost node can be a
  left child if the right subtree is missing.
- Capturing `queue[0]` instead of the last element of the level.

## Related problems

- 102 Binary Tree Level Order Traversal
- 515 Find Largest Value in Each Tree Row
- 116 Populating Next Right Pointers in Each Node
