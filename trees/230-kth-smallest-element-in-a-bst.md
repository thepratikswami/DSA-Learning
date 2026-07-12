# 230. Kth Smallest Element in a BST

- **Difficulty:** Medium
- **Pattern:** trees
- **Companies:** Amazon, Google, Meta, Microsoft, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return the `k`-th smallest value in a binary search tree (1-indexed).

## Approaches

### Brute force

Collect every value with an inorder traversal into a list, then return the
element at index `k - 1`.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

Iterative inorder traversal with an explicit stack. Push all left children, then
pop and decrement `k`; when `k` reaches `0` the current node is the answer, so we
stop early without visiting the whole tree.

- Time: `O(h + k)`
- Space: `O(h)`

## Key insight

Inorder traversal of a BST visits values in ascending order, so the `k`-th popped
node is exactly the `k`-th smallest, and we can halt as soon as it is found.

## Edge cases

- `k = 1` returns the leftmost node.
- `k` equal to the node count returns the maximum.
- Left- or right-skewed trees.

## Pitfalls

- Decrementing `k` before popping, throwing off the count.
- Continuing traversal after the answer is found instead of returning early.

## Related problems

- 94 Binary Tree Inorder Traversal
- 173 Binary Search Tree Iterator
- 700 Search in a Binary Search Tree
- 671 Second Minimum Node In a Binary Tree
