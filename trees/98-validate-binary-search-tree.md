# 98. Validate Binary Search Tree

- **Difficulty:** Medium
- **Pattern:** trees
- **Companies:** Amazon, Meta, Microsoft, Google, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Determine whether a binary tree is a valid BST: every node's value must be
strictly greater than all values in its left subtree and strictly less than all
values in its right subtree.

## Approaches

### Brute force

For each node, walk its entire left subtree to confirm all values are smaller and
its entire right subtree to confirm all are larger.

- Time: `O(n^2)`
- Space: `O(h)`

### Optimal

DFS carrying an open `(low, high)` bound. Each node must satisfy
`low < val < high`; recurse left with `high = val` and right with `low = val`,
starting from `(-inf, +inf)`.

- Time: `O(n)`
- Space: `O(h)`

## Key insight

Validity is a range constraint inherited from all ancestors, not just the direct
parent, so passing tightening bounds down captures the full-subtree rule in one
pass.

## Edge cases

- Empty tree is valid.
- Duplicate values are invalid (strict inequality).
- Extreme `INT_MIN` / `INT_MAX` node values — using infinite sentinels avoids
  boundary bugs.

## Pitfalls

- Comparing only against the immediate parent instead of inherited bounds.
- Using `<=` / `>=` and wrongly accepting duplicates.

## Related problems

- 700 Search in a Binary Search Tree
- 230 Kth Smallest Element in a BST
- 99 Recover Binary Search Tree
- 501 Find Mode in Binary Search Tree
