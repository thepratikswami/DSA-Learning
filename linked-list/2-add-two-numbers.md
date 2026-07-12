# 2. Add Two Numbers

- **Difficulty:** Medium
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Bloomberg, Google, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/add-two-numbers/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Two non-empty linked lists represent two non-negative integers with digits stored in
reverse order. Add the numbers and return the sum as a linked list, also in reverse
order.

## Approaches

### Optimal

Walk both lists in lockstep with a running `carry`. At each step sum the available
digits plus the carry, use `divmod(total, 10)` to split into the new carry and the
stored digit, and append a node. Continue while either list has nodes or a carry
remains.

- Time: `O(max(n, m))`
- Space: `O(max(n, m))` for the output list

## Key insight

Reverse-order storage means you process least-significant digits first, exactly the
order addition needs, so a single forward pass with a carry works.

## Edge cases

- Different-length numbers.
- A final carry that grows the result by one digit (e.g. `5 + 5 = 10`).
- One list longer than the other.

## Pitfalls

- Stopping the loop before flushing a leftover carry.
- Forgetting to advance a list only when it still has nodes.

## Related problems

- 445 Add Two Numbers II
- 43 Multiply Strings
- 67 Add Binary
