# 162. Find Peak Element

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/find-peak-element/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given an array where `nums[i] != nums[i+1]`, return the index of any peak element
(greater than both neighbors), treating out-of-bounds as negative infinity, in
`O(log n)`.

## Approaches

### Brute force

Scan and return the first index that is greater than both its neighbors.

- Time: `O(n)`
- Space: `O(1)`

### Optimal

Binary search with `while left < right`. Compare `nums[mid]` to `nums[mid + 1]`:
if `nums[mid] < nums[mid + 1]` a peak lies to the right (`left = mid + 1`);
otherwise a peak is at `mid` or to the left (`right = mid`). `left` lands on a peak.

- Time: `O(log n)`
- Space: `O(1)`

## Key insight

Following the ascending slope always leads toward a peak, because the array
boundaries act as negative infinity, so a rising direction guarantees a peak ahead.

## Edge cases

- Single element (it is a peak).
- Strictly increasing array (peak is the last element).
- Strictly decreasing array (peak is the first element).

## Pitfalls

- Accessing `nums[mid + 1]` is safe only because `left < right` keeps `mid + 1`
  in range.
- Trying to find "the" peak; any peak is acceptable.

## Related problems

- 852 Peak Index in a Mountain Array
- 153 Find Minimum in Rotated Sorted Array
- 33 Search in Rotated Sorted Array
