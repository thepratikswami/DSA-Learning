# 380. Insert Delete GetRandom O(1)

- **Difficulty:** Medium
- **Pattern:** design
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/insert-delete-getrandom-o1/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Design a set supporting `insert`, `remove`, and `getRandom` in average `O(1)`
time, where `getRandom` returns each element with equal probability.

## Approaches

### Hash map + dynamic array with swap-to-last

Store values in a list for `O(1)` random indexing, and a hash map of
`value -> index` for `O(1)` lookup. To remove, swap the target with the last
element, update the moved element's index, then pop the tail.

- Time: `O(1)` average per operation
- Space: `O(n)`

## Key insight

`getRandom` needs contiguous indices, which a list provides but a plain set
does not. Swap-with-last removal keeps the list dense in `O(1)` without shifting
elements.

## Edge cases

- Removing the last element (swap is a no-op, just pop).
- Inserting a value already present returns `False`.
- Removing a value that is absent returns `False`.

## Pitfalls

- Using `list.remove` or `list.index`, which are `O(n)`.
- Forgetting to update the moved element's index in the map after the swap.
- Leaving the removed key in the hash map.

## Related problems

- 381 Insert Delete GetRandom O(1) - Duplicates allowed
- 528 Random Pick with Weight
- 710 Random Pick with Blacklist
