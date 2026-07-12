# 143. Reorder List

- **Difficulty:** Medium
- **Pattern:** linked-list
- **Companies:** Amazon, Meta, Microsoft, Google, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/reorder-list/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Reorder a list `L0 -> L1 -> ... -> Ln` in place to
`L0 -> Ln -> L1 -> Ln-1 -> ...` without changing node values.

## Approaches

### Brute force

Copy all nodes into an array for random access, then rewire links by picking from
the front and back alternately.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

Three classic steps in place: (1) find the middle with slow/fast pointers, (2)
reverse the second half, (3) merge the two halves node by node, splicing back-half
nodes between front-half nodes.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

The target order is a front-to-back interleave; getting there is just find-middle +
reverse-second-half + alternate-merge, all with pointer surgery.

## Edge cases

- Empty list or single node (return immediately).
- Two-node list stays unchanged.
- Odd vs even length: the split point differs by one.

## Pitfalls

- Not cutting the first half with `slow.next = None`, leaving a cycle.
- Losing successor references during reversal and the merge.
- Using `head, head.next` as the initial slow/fast pair affects where the middle lands.

## Related problems

- 206 Reverse Linked List
- 876 Middle of the Linked List
- 234 Palindrome Linked List
- 21 Merge Two Sorted Lists
