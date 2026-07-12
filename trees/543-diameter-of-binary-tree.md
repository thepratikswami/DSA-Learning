# 543. Diameter of Binary Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/diameter-of-binary-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the length of the longest path between any two nodes in the tree, measured
in edges. The path may or may not pass through the root.

## Approaches

### Post-order DFS with a running max

Compute each node's height. The longest path that *bends* at a node is
`leftHeight + rightHeight` (in edges). Track the global max while returning
`1 + max(left, right)` upward.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

The answer at every node is "left height + right height in edges"; the diameter
is the maximum of that quantity over all nodes, computed in one traversal.

## Edge cases

- Empty tree returns `0`.
- Single node returns `0` (no edges).
- Skewed tree returns `n - 1`.

## Pitfalls

- Confusing edge count with node count (off-by-one).
- Returning the diameter from the recursion instead of the height.

## Related problems

- 104 Maximum Depth of Binary Tree
- 124 Binary Tree Maximum Path Sum
- 687 Longest Univalue Path
