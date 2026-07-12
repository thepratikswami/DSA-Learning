# 26. Remove Duplicates from Sorted Array

- **Difficulty:** Easy
- **Pattern:** two-pointers
- **Companies:** Amazon, Microsoft, Google, Apple, Bloomberg
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given a sorted array `nums`, remove duplicates in place so each value appears
once and return the count `k` of unique elements (the first `k` slots hold them).

## Approaches

### Optimal

Use a same-direction two-pointer scan: `read` scans every element while `write`
marks the next slot for a unique value. Whenever `nums[read]` differs from the
last written value `nums[write - 1]`, copy it forward and advance `write`. Return
`write` as the new length.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

Because the array is sorted, duplicates are adjacent, so comparing against the
last written element is enough to detect a new unique value.

## Edge cases

- Empty array (return 0).
- All identical elements (return 1).
- Already fully unique array.

## Pitfalls

- Comparing `nums[read]` with `nums[read - 1]` instead of the last *written*
  value, which breaks when runs are long.
- Returning the modified array instead of the length `k`.

## Related problems

- 27 Remove Element
- 80 Remove Duplicates from Sorted Array II
- 283 Move Zeroes
