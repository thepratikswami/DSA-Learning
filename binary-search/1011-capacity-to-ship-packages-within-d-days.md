# 1011. Capacity To Ship Packages Within D Days

- **Difficulty:** Medium
- **Pattern:** binary-search
- **Companies:** Amazon, Google, Microsoft, Meta, Bloomberg

- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

Packages with given `weights` must ship in their given order within `days` days.
Find the minimum ship capacity that allows completing within `days`.

## Approaches

### Brute force

Try every candidate capacity from `max(weights)` upward, simulating the number of
days needed until you find the first capacity that fits within `days`.

- Time: `O(sum(weights) * n)`
- Space: `O(1)`

### Optimal

Binary search on capacity in `[max(weights), sum(weights)]`. The check
`can_ship(capacity)` greedily accumulates weights, starting a new day whenever the
next package would overflow, and tests `used_days <= days`. Feasibility is
monotonic, so converge to the smallest feasible capacity.

- Time: `O(n * log(sum(weights)))`
- Space: `O(1)`

## Key insight

The low bound must be `max(weights)` (a single package must fit) and the high bound
`sum(weights)` (ship everything in one day); larger capacity never needs more days.

## Edge cases

- `days == 1` forces capacity equal to `sum(weights)`.
- `days >= len(weights)` allows capacity equal to `max(weights)`.
- All weights equal.

## Pitfalls

- Starting the low bound below `max(weights)` yields an infeasible answer.
- Off-by-one in the greedy day counter (start `used_days = 1`).

## Related problems

- 875 Koko Eating Bananas
- 410 Split Array Largest Sum
- 1482 Minimum Number of Days to Make m Bouquets
