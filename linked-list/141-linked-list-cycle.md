# 141. Linked List Cycle

- **Difficulty:** Easy
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/linked-list-cycle/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Return whether a singly linked list contains a cycle.

## Approaches

### Brute force

Store every visited node in a hash set; a cycle exists if you revisit a node.

- Time: `O(n)`
- Space: `O(n)`

### Optimal

Floyd's tortoise and hare. Advance `slow` by one and `fast` by two each step; if
they ever meet there is a cycle, and if `fast` reaches the end there is none.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Inside a cycle the fast pointer gains one node per step on the slow pointer, so it
must eventually land on it; without a cycle `fast` simply runs off the end.

## Edge cases

- Empty list or single node with no `next`.
- Single node pointing to itself.
- Cycle back to the head.

## Pitfalls

- Checking `fast and fast.next` before dereferencing `fast.next.next`.
- Comparing node identity (`is`), not values.
- Starting the pointers offset can miss the first-step meeting; start both at head.

## Related problems

- 142 Linked List Cycle II
- 202 Happy Number
- 287 Find the Duplicate Number
- 876 Middle of the Linked List
