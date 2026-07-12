# 25. Reverse Nodes in k-Group

- **Difficulty:** Hard
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Meta, Google, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/reverse-nodes-in-k-group/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Reverse the nodes of a linked list `k` at a time and return the modified list. If the
number of remaining nodes is fewer than `k`, leave them as-is. Only node links may be
changed, not values.

## Approaches

### Optimal

Use a `dummy` and a `group_prev` marker. For each group, walk `k` steps to find the
`kth` node; if fewer than `k` nodes remain, stop. Reverse the group in place using the
node after the group (`group_next`) as the initial `prev`, then reconnect: `group_prev`
points to the new head (`kth`) and the old head becomes the next `group_prev`.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Reversing a fixed-size window is standard pointer reversal; the extra bookkeeping is
just reconnecting the reversed block to the nodes before and after it.

## Edge cases

- `k == 1` returns the list unchanged.
- List length not a multiple of `k` leaves the final short group in original order.
- `k` equal to the list length reverses the whole list.

## Pitfalls

- Reversing a trailing group that has fewer than `k` nodes.
- Losing the connection between consecutive groups (track `group_prev` and the old head).

## Related problems

- 206 Reverse Linked List
- 92 Reverse Linked List II
- 24 Swap Nodes in Pairs
