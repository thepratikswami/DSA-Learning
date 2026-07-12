# 33. Search in Rotated Sorted Array

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg, Apple

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

A sorted array of distinct integers is rotated at an unknown pivot. Find the index
of `target` in `O(log n)`, or return `-1`.

## Approaches

### Brute force

Linear scan the whole array for `target`.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Modified binary search. At each `mid`, exactly one half is sorted. If the left half
`nums[left..mid]` is sorted (`nums[left] <= nums[mid]`), check whether `target`
lies in that range and discard accordingly; otherwise the right half is sorted and
apply the symmetric check.

- Time: `O(log n)`
- Space: `O(1)`

## Key insight

Even after rotation, any midpoint splits the array so that at least one side is
fully sorted, letting you decide in `O(1)` which half can contain the target.

## Edge cases

- Not rotated at all (already sorted).
- Target at the pivot boundary.
- Single element or two-element arrays.

## Pitfalls

- Using strict `<` vs `<=` when testing `nums[left] <= nums[mid]` matters for the
  two-element case.
- Getting the inclusive range checks (`nums[left] <= target < nums[mid]`) backwards.

## Related problems

- 81 Search in Rotated Sorted Array II
- 153 Find Minimum in Rotated Sorted Array
- 162 Find Peak Element
