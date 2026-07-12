# 236. Lowest Common Ancestor of a Binary Tree

- **Difficulty:** Medium
- **Pattern:** trees
- **Companies:** Meta, Amazon, Microsoft, Google, LinkedIn, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given two nodes `p` and `q` in a binary tree, return their lowest common
ancestor (the deepest node that has both in its subtree).

## Approaches

### Optimal

Post-order DFS. Return the node when it matches `p`, `q`, or is `None`. If both
the left and right recursive calls return non-null, the current node is the LCA;
otherwise bubble up whichever side is non-null.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

If `p` and `q` are found in different subtrees of a node, that node is their LCA;
if both are in the same subtree, the answer propagates up from that side.

## Edge cases

- One node is an ancestor of the other (returns the ancestor).
- `p` or `q` is the root.
- Both targets are guaranteed to exist per constraints.

## Pitfalls

- Comparing by value instead of identity (`is`) when duplicates are possible.
- Returning too early and missing the "found in both subtrees" case.

## Related problems

- 235 Lowest Common Ancestor of a Binary Search Tree
- 1650 Lowest Common Ancestor of a Binary Tree III
- 1123 Lowest Common Ancestor of Deepest Leaves
