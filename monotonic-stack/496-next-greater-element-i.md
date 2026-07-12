# 496. Next Greater Element I

- **Difficulty:** Easy
- **Pattern:** monotonic-stack
- **Companies:** Amazon, Microsoft, Bloomberg, Adobe
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/next-greater-element-i/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

`nums1` is a subset of `nums2`. For each value in `nums1`, find the first
element to its right in `nums2` that is greater than it; return `-1` if none
exists.

## Approaches

### Brute force

For each value in `nums1`, locate it in `nums2` and scan right until a greater
value appears.

- Time: `O(n * m)`
- Space: `O(1)`

### Optimal

Scan `nums2` once with a decreasing monotonic stack. When the current value
exceeds the stack top, that value is the top's next greater element; record it in
a hash map. Answer each `nums1` query with an `O(1)` lookup.

- Time: `O(n + m)`
- Space: `O(m)`

## Key insight

A decreasing stack resolves every element the moment a larger value appears, so
one pass over `nums2` precomputes all answers.

## Edge cases

- Values in `nums1` with no greater element to the right -> `-1`.
- `nums2` strictly decreasing (nothing is ever popped early).

## Pitfalls

- Comparing values instead of using `stack[-1] < x` on the stored value.
- Forgetting the default `-1` for values never popped.

## Related problems

- 503 Next Greater Element II (monotonic-stack)
- 739 Daily Temperatures (stack)
- 901 Online Stock Span (monotonic-stack)
