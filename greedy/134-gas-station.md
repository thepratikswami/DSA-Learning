# 134. Gas Station

- **Difficulty:** Medium
- **Pattern:** greedy
- **Companies:** Amazon, Google, Microsoft, Bloomberg, Uber
- **Last reviewed:** 2026-07-09
- **LeetCode:** https://leetcode.com/problems/gas-station/

> Company tags are a curated, approximate "frequently asked at" list and change
> over time. Treat them as prioritization hints, not authoritative data.

## Problem

There are `n` gas stations on a circular route. `gas[i]` is the fuel available at
station `i` and `cost[i]` is the fuel needed to travel from `i` to `i + 1`.
Return the starting station index from which you can complete the full circuit
once, or `-1` if impossible. The answer is guaranteed unique when it exists.

## Approaches

### Brute force

Try each station as a start and simulate the whole loop.

- Time: `O(n^2)`
- Space: `O(1)`

### Optimal

If the total gas is at least the total cost, a solution exists. Sweep once,
accumulating `gas[i] - cost[i]`. Whenever the running tank drops below zero, no
station in the current window can be the start, so reset the candidate start to
the next station and zero the tank.

- Time: `O(n)`
- Space: `O(1)`

## Key insight

If you run out of gas somewhere between `start` and `i`, every station in that
range fails too, so you can skip straight to `i + 1` instead of retrying each.

## Edge cases

- Total gas less than total cost: return `-1`.
- Single station where `gas[0] >= cost[0]`.

## Pitfalls

- Resetting the tank but forgetting to move the candidate start.
- Trying to return early before confirming the global feasibility check.

## Related problems

- 55 Jump Game
- 45 Jump Game II
- 53 Maximum Subarray
