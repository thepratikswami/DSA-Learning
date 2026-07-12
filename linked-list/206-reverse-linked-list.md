# 206. Reverse Linked List

- **Difficulty:** Easy
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Google, Meta, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/reverse-linked-list/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Reverse a singly linked list and return the new head.

## Approaches

### Optimal

Iterate with three roles: `prev` (built reversed part), `curr` (node being moved),
and a saved `next_node`. Each step points `curr.next` back to `prev`, then slides
all pointers forward. When `curr` is `None`, `prev` is the new head.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Reversal is just flipping one link at a time while remembering the next node so the
tail of the list is never lost.

## Edge cases

- Empty list returns `None`.
- Single node returns itself.
- Two-node list swaps head and tail.

## Pitfalls

- Overwriting `curr.next` before saving `next_node` disconnects the rest of the list.
- Returning `curr` (now `None`) instead of `prev`.
- A recursive version costs `O(n)` stack space.

## Related problems

- 92 Reverse Linked List II
- 25 Reverse Nodes in k-Group
- 234 Palindrome Linked List
- 143 Reorder List
