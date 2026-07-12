# 1482. Minimum Number of Days to Make m Bouquets

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Uber

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Each flower blooms on day `bloomDay[i]`. You need `m` bouquets, each using `k`
adjacent bloomed flowers. Return the minimum day to make all bouquets, or `-1` if
impossible.

## Approaches

### Brute force

Try each candidate day from `min(bloomDay)` upward, scanning the garden to count
buildable bouquets until you find the first feasible day.

- Time: `O(max(bloomDay) * n)`
- Space: `O(1)`

### Optimal

First rule out impossibility with `m * k > len(bloomDay)`. Then binary search the
day in `[min(bloomDay), max(bloomDay)]`. The check `can_make(day)` walks the array
counting runs of `k` consecutive flowers already bloomed by `day`, resetting the
run when a flower has not bloomed, and tests `bouquets >= m`.

- Time: `O(n * log(max(bloomDay)))`
- Space: `O(1)`

## Key insight

Waiting more days only bloom more flowers, so "can make m bouquets by day d" is
monotonic in `d`, enabling binary search on the day.

## Edge cases

- `m * k > len(bloomDay)` is impossible, return `-1`.
- `k == 1` (any bloomed flower is a bouquet).
- All flowers bloom on the same day.

## Pitfalls

- Forgetting to reset the consecutive counter when a flower has not yet bloomed.
- Counting overlapping windows instead of non-overlapping adjacent groups.

## Related problems

- 875 Koko Eating Bananas
- 1011 Capacity to Ship Packages Within D Days
- 410 Split Array Largest Sum
