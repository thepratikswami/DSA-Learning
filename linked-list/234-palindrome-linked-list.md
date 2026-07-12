# 234. Palindrome Linked List

- **Difficulty:** Easy
- **Pattern:** linked-list
- **Companies:** Amazon, Microsoft, Meta, Apple, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/palindrome-linked-list/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given the head of a singly linked list, return `True` if it reads the same forwards and
backwards.

## Approaches

### Reverse second half (optimal)

Find the middle with slow/fast pointers, reverse the second half in place, then compare
it node-by-node against the first half. Stops when the reversed (shorter or equal) half
is exhausted.

- Time: `O(n)`
- Space: `O(1)`

### Copy to array

Dump values into a list and check with two-pointer comparison. Simpler but uses `O(n)`
extra space.

## Key insight

You only need to compare the first half with the reversed second half; the middle node
of an odd-length list never needs a partner.

## Edge cases

- Empty list and single node are palindromes.
- Even vs odd length changes where the middle lands.
- All-equal values.

## Pitfalls

- Comparing past the shorter half (loop on the reversed `right`, not `left`).
- Mutating the list is fine here, but restore it if the caller reuses the list.

## Related problems

- 206 Reverse Linked List
- 143 Reorder List
- 9 Palindrome Number
