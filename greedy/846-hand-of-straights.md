# 846. Hand of Straights

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Google, Amazon, Microsoft, Apple
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/hand-of-straights/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array `hand` of card values and an integer `groupSize`, return whether
the cards can be rearranged into groups of `groupSize` consecutive cards.

## Approaches

### Optimal (count + min-heap)

Count each card value. Repeatedly take the smallest remaining value and try to
form a run of `groupSize` consecutive values starting there, decrementing counts.
If any needed card is missing, return `False`. A min-heap keeps the smallest
available value at hand.

- Time: `O(n log n)`
- Space: `O(n)`

## Key insight

The smallest remaining card must be the start of some group, because nothing
smaller exists to precede it. That forces the rest of its run deterministically.

## Edge cases

- `len(hand)` not divisible by `groupSize`: immediately impossible.
- `groupSize == 1`: always possible.

## Pitfalls

- Only removing a value from the heap when its count reaches zero, and requiring
  that a depleted card be the current minimum (otherwise ordering breaks).
- Forgetting the divisibility precheck.

## Related problems

- 1296 Divide Array in Sets of K Consecutive Numbers
- 659 Split Array into Consecutive Subsequences
