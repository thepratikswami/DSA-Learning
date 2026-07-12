# 81. Search in Rotated Sorted Array II

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Microsoft, Google, Bloomberg, Meta

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Like problem 33, but the rotated sorted array may contain duplicates. Return
whether `target` exists.

## Approaches

### Brute force

Linear scan the whole array.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Same rotated binary search as 33, plus a duplicate-handling branch: when
`nums[left] == nums[mid] == nums[right]`, you cannot tell which half is sorted, so
shrink both ends (`left += 1`, `right -= 1`). Otherwise identify the sorted half
and discard as usual.

- Time: `O(log n)` average, `O(n)` worst case with many duplicates
- Space: `O(1)`

## Key insight

Duplicates can make `nums[left] == nums[mid] == nums[right]`, hiding which side is
sorted; the only safe move is to trim both boundaries by one and retry.

## Edge cases

- Array of all identical values.
- Target absent among many duplicates.
- Not actually rotated.

## Pitfalls

- Forgetting the `nums[left] == nums[mid] == nums[right]` branch causes wrong
  half-selection.
- Assuming `O(log n)` worst case; duplicates degrade it to `O(n)`.

## Related problems

- 33 Search in Rotated Sorted Array
- 153 Find Minimum in Rotated Sorted Array
- 154 Find Minimum in Rotated Sorted Array II
