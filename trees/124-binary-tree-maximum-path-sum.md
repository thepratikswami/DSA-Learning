# 124. Binary Tree Maximum Path Sum

- **Difficulty:** Hard
- **Pattern:** trees
- **Companies:** Amazon, Meta, Google, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

A path is any sequence of connected nodes (each pair joined by an edge). Return
the maximum sum of node values over all non-empty paths; a path need not pass
through the root.

## Approaches

### Post-order DFS with a global max

For each node compute the max downward gain of each child, clamped at `0` (drop a
negative branch). The best path *bending* at this node is
`node.val + leftGain + rightGain`; update the global max with it. Return
`node.val + max(leftGain, rightGain)` so the parent can extend a single branch.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

Separate two quantities: the answer that bends at a node (uses both children) vs.
the value returned upward (only one child, since a parent can't reuse both).

## Edge cases

- All-negative tree returns the largest single value, not `0`.
- Single node returns its own value.
- Mixed signs where skipping a subtree beats including it.

## Pitfalls

- Returning the bending sum upward instead of the single-branch extension.
- Initializing the answer to `0` and missing all-negative inputs; use `-inf`.

## Related problems

- 543 Diameter of Binary Tree
- 687 Longest Univalue Path
- 129 Sum Root to Leaf Numbers
