# 153. Find Minimum in Rotated Sorted Array

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Microsoft, Google, Meta, Bloomberg, Apple

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

A sorted array of distinct integers is rotated at an unknown pivot. Return the
minimum element in `O(log n)`.

## Approaches

### Brute force

Scan every element and track the minimum.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Binary search with `while left < right`, comparing `nums[mid]` to `nums[right]`.
If `nums[mid] > nums[right]` the minimum must be to the right, so `left = mid + 1`;
otherwise it is at `mid` or to the left, so `right = mid`. `left` converges on the
minimum.

- Time: `O(log n)`
- Space: `O(1)`

## Key insight

Comparing against the right end tells you which side holds the rotation point: a
midpoint bigger than the rightmost value means the drop is still ahead.

## Edge cases

- Array not rotated (minimum is the first element).
- Two-element array.
- Single element.

## Pitfalls

- Comparing `nums[mid]` to `nums[left]` instead of `nums[right]` fails on
  non-rotated inputs.
- Using `left <= right` risks moving past the answer; use `left < right`.

## Related problems

- 154 Find Minimum in Rotated Sorted Array II
- 33 Search in Rotated Sorted Array
- 162 Find Peak Element
