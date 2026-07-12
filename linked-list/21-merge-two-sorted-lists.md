# 21. Merge Two Sorted Lists

- **Difficulty:** Easy
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Apple, Adobe, Meta
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given the heads of two sorted linked lists `list1` and `list2`, splice them into
one sorted list and return its head.

## Approaches

### Optimal

Use a `dummy` head and a `curr` tail. Compare the front nodes of each list, attach
the smaller one to `curr`, and advance that list. When one list runs out, attach the
remaining nodes of the other directly.

- Time: `O(n + m)`
- Space: `O(1)`

## Key insight

A dummy node removes the "is this the first node?" special case, so every append is
the same operation.

## Edge cases

- One or both lists empty.
- Equal values across lists (stability does not matter but `<=` keeps order predictable).
- Lists of very different lengths.

## Pitfalls

- Forgetting to attach the leftover tail after the loop.
- Creating new nodes instead of relinking existing ones (wastes space).

## Related problems

- 23 Merge k Sorted Lists
- 88 Merge Sorted Array
- 148 Sort List
