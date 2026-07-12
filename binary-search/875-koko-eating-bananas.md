# 875. Koko Eating Bananas

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Meta, Microsoft, Bloomberg, Uber

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/koko-eating-bananas/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Given `piles` of bananas and `h` hours, find the minimum integer eating speed `k`
such that Koko can finish all bananas within `h` hours (one pile per hour, ceiling
division per pile).

## Approaches

### Brute force

Try every candidate speed from `1` upward, and for each simulate the total hours
until you find the first speed that finishes within `h`.

- Time: `O(max(piles) * n)`
- Space: `O(1)`

### Optimal

Binary search on the answer space of speeds `[1, max(piles)]`. The feasibility
check `can_finish(speed)` sums `ceil(pile / speed)` hours and tests `<= h`. Since
feasibility is monotonic in speed, shrink toward the smallest feasible speed with
`right = mid` on success and `left = mid + 1` on failure.

- Time: `O(n * log(max(piles)))`
- Space: `O(1)`

## Key insight

Faster speed never needs more hours, so "can finish at this speed" is monotonic —
false for slow speeds, true for fast — making it a binary search on the answer.

## Edge cases

- `h == len(piles)` forces speed equal to `max(piles)`.
- A single huge pile dominates the required speed.
- `h` much larger than the number of piles allows a slow speed.

## Pitfalls

- Using floor instead of ceiling division miscounts hours per pile.
- Setting the low bound to `0` (speed must be at least `1`).

## Related problems

- 1011 Capacity to Ship Packages Within D Days
- 1482 Minimum Number of Days to Make m Bouquets
- 410 Split Array Largest Sum
