# 19. Remove Nth Node From End of List

- **Difficulty:** Medium
- **Pattern:** linked-list
- **Companies:** Amazon, Meta, Microsoft, Google, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Remove the `n`-th node counted from the end of a singly linked list and return the
head.

## Approaches

### Brute force

First pass to compute length `L`, second pass to walk `L - n` steps and unlink.

- Time: `O(n)` (two passes)
- Space: `O(1)`

### Optimal

One pass with a gap. Use a dummy before the head; advance `fast` `n` steps first,
then move `fast` and `slow` together until `fast.next` is `None`. `slow` now sits
just before the target, so `slow.next = slow.next.next` removes it.

- Time: `O(n)` (single pass)
- Space: `O(1)`

## Key insight

Keeping a fixed gap of `n` between two pointers means when the leader reaches the
last node, the follower is exactly one before the node to delete.

## Edge cases

- Removing the head (`n == length`), handled cleanly by the dummy node.
- Single-node list where `n == 1`.
- `n` equal to the list length.

## Pitfalls

- Skipping the dummy node makes head removal a special case.
- Advancing `fast` the wrong number of steps (off-by-one on the gap).
- Stopping on `fast` instead of `fast.next`, landing on the target rather than before it.

## Related problems

- 876 Middle of the Linked List
- 2095 Delete the Middle Node of a Linked List
- 203 Remove Linked List Elements
- 1721 Swapping Nodes in a Linked List
