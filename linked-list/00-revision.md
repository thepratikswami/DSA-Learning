# Linked List Interview Revision

## Core idea

Manipulate node references carefully. Save the next node before changing links.

## How to recognize it

- The problem gives `ListNode`.
- You need to reverse, remove, merge, or reorder nodes.
- Index-based access is not available.
- Fast and slow pointers can reveal a middle or cycle.

## Interview thinking steps

1. Decide whether a dummy node helps.
2. Track the important pointers before mutating links.
3. Handle empty list, one node, and head removal.
4. For nth-from-end, use a gap between two pointers.
5. For cycle detection, use fast and slow pointers.

## Pitfalls

- Losing the rest of the list after changing `curr.next`.
- Forgetting to update `head` when the first node changes.
- Infinite loops caused by stale links.
- Off-by-one errors in nth-from-end removal.

## Complexity

Most linked-list pointer solutions are `O(n)` time and `O(1)` extra space.
