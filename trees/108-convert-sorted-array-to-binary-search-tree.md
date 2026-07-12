# 108. Convert Sorted Array to Binary Search Tree

- **Difficulty:** Easy
- **Pattern:** trees
- **Companies:** Amazon, Google, Microsoft, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Turn a sorted ascending array into a height-balanced BST.

## Approaches

### Optimal

Divide and conquer over index bounds: pick the middle element as the root, then
recursively build the left subtree from the left half and the right subtree from
the right half.

- Time: `O(n)`
- Space: `O(log n)`

## Key insight

Because the array is sorted, the middle element keeps the two halves balanced and
naturally satisfies the BST ordering, so always choosing the midpoint yields a
height-balanced tree.

## Edge cases

- Empty array returns `None`.
- Single element becomes the root leaf.
- Even-length ranges: either midpoint choice is valid.

## Pitfalls

- Off-by-one errors in the `left > right` base case or `mid` computation.
- Picking a non-middle pivot, which loses the balance guarantee.

## Related problems

- 109 Convert Sorted List to Binary Search Tree
- 1382 Balance a Binary Search Tree
- 95 Unique Binary Search Trees II
