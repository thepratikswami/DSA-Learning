# 110. Balanced Binary Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Amazon, Google, Microsoft, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/balanced-binary-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return `True` if the tree is height-balanced: for every node, the heights of its
two subtrees differ by at most `1`.

## Approaches

### Naive top-down

For each node compute the height of both subtrees and check the balance
condition. Recomputing height at every node is `O(n^2)` in the worst case.

- Time: `O(n^2)`
- Space: `O(h)`

### Optimal bottom-up

Return the height from the recursion, but use a sentinel `-1` to signal that a
subtree is already unbalanced, short-circuiting the rest.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

Fusing the height computation with the balance check into a single post-order
pass avoids recomputing heights, dropping the cost from `O(n^2)` to `O(n)`.

## Edge cases

- Empty tree is balanced (`True`).
- Single node is balanced.
- A subtree deep down being unbalanced must fail the whole tree.

## Pitfalls

- Forgetting to propagate the `-1` sentinel upward once found.
- Using a top-down approach that recomputes height and times out on large trees.

## Related problems

- 104 Maximum Depth of Binary Tree
- 543 Diameter of Binary Tree
- 108 Convert Sorted Array to Binary Search Tree
