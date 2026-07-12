# 622. Design Circular Queue

- **Difficulty:** Medium
- **Pattern:** design
- **Companies:** Amazon, Microsoft, Google, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/design-circular-queue/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a fixed-size circular queue supporting `enQueue`, `deQueue`, `Front`,
`Rear`, `isEmpty`, and `isFull`, all in `O(1)` time.

## Approaches

### Fixed array with head and count

Allocate an array of size `k`. Track `head` (index of the front) and `count`
(number of stored elements). The rear index is `(head + count - 1) % k` and the
next insertion slot is `(head + count) % k`.

- Time: `O(1)` per operation
- Space: `O(k)`

## Key insight

Tracking `head` and `count` avoids the classic ambiguity between a full and an
empty queue that arises when using only `head` and `tail` pointers.

## Edge cases

- `enQueue` on a full queue returns `False`.
- `deQueue` on an empty queue returns `False`.
- `Front` and `Rear` on an empty queue return `-1`.
- Wrap-around when the rear index exceeds the array end.

## Pitfalls

- Confusing full vs empty when only two pointers are used.
- Off-by-one errors in the modular rear/insert index.
- Forgetting to decrement `count` on `deQueue`.

## Related problems

- 641 Design Circular Deque
- 232 Implement Queue using Stacks
- 1670 Design Front Middle Back Queue
