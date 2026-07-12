# 410. Split Array Largest Sum

- **Difficulty:** Hard
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/split-array-largest-sum/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Split `nums` into `k` non-empty contiguous subarrays so that the largest subarray
sum is minimized, and return that minimized largest sum.

## Approaches

### Brute force

Try every candidate limit for the largest sum from `max(nums)` upward, greedily
counting how many parts each limit requires until one fits within `k`. (A DP over
splits is the classic non-search alternative.)

- Time: `O(sum(nums) * n)` for the search sweep
- Space: `O(1)`

### Optimal

Binary search on the answer (the largest allowed subarray sum) in
`[max(nums), sum(nums)]`. The check `can_split(limit)` greedily grows a running
sum, starting a new part when it would exceed `limit`, and tests `parts <= k`.
Feasibility is monotonic, so converge to the smallest feasible limit.

- Time: `O(n * log(sum(nums)))`
- Space: `O(1)`

## Key insight

A larger allowed sum never needs more parts, so "can split into <= k parts under
this limit" is monotonic — the minimized largest sum is the smallest feasible limit.

## Edge cases

- `k == 1` gives `sum(nums)`.
- `k >= len(nums)` gives `max(nums)`.
- Single element array.

## Pitfalls

- Low bound must be `max(nums)`, since any single element must fit in one part.
- Off-by-one in the greedy part counter (start `parts = 1`).

## Related problems

- 1011 Capacity to Ship Packages Within D Days
- 875 Koko Eating Bananas
- 1482 Minimum Number of Days to Make m Bouquets
