# 104. Maximum Depth of Binary Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Amazon, Google, Apple, Microsoft, LinkedIn
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the number of nodes along the longest path from the root down to the
farthest leaf.

## Approaches

### Optimal

Post-order DFS: the depth of a node is `1 + max(depth(left), depth(right))`, with
a `None` node contributing depth `0`.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

Each node's answer depends only on its children's answers, so a single recursive
return value collapses the whole subtree into one number.

## Edge cases

- Empty tree returns `0`.
- Single node returns `1`.
- Fully skewed tree returns `n`.

## Pitfalls

- Returning the max child depth without adding `1` for the current node.
- Recursion depth blowing the stack on a degenerate (linked-list) tree.

## Related problems

- 111 Minimum Depth of Binary Tree
- 110 Balanced Binary Tree
- 543 Diameter of Binary Tree
- 559 Maximum Depth of N-ary Tree
